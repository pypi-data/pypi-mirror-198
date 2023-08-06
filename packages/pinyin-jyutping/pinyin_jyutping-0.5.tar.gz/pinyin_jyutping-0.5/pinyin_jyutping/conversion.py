import jieba
import logging
import copy
import pprint
from . import syllables
from . import logic
from . import constants

logger = logging.getLogger(__file__)


def fill_romanization_solution_for_characters(word_map, characters, current_solution, all_solutions):
    if len(characters) == 0:
        all_solutions.append(current_solution)
        return
    current_character = characters[0]    
    remaining_characters = characters[1:]
    entry = word_map.get(current_character, None)
    if entry != None:
        for result in entry:
            new_solution = copy.copy(current_solution)
            new_solution.append(result.syllables[0])
            fill_romanization_solution_for_characters(word_map, remaining_characters, new_solution, all_solutions)
    else:
        # implement pass through syllable here
        syllable = syllables.PassThroughSyllable(current_character)
        new_solution = copy.copy(current_solution)
        new_solution.append(syllable)
        fill_romanization_solution_for_characters(word_map, remaining_characters, new_solution, all_solutions)        

def get_romanization_solutions_for_characters(word_map, word):
    all_solutions = []
    fill_romanization_solution_for_characters(word_map, word, [], all_solutions)
    return all_solutions

def get_romanization_solutions_for_word(word_map, word):
    entry = word_map.get(word, None)
    if entry != None:
        logger.debug(f'located {word} as word')
        return [mapping.syllables for mapping in entry]
    else:
        logger.debug(f'breaking down {word} into characters')
        return get_romanization_solutions_for_characters(word_map, word)

def get_romanization_solutions(word_map, word_list):
    return [get_romanization_solutions_for_word(word_map, word) for word in word_list]


def expand_solutions(word_map, word_list, current_solution, expanded_solution_list):
    if len(word_list) == 0:
        expanded_solution_list.append(current_solution)
        return

    current_word = word_list[0]
    remaining_words = word_list[1:]

    for alternative in current_word:
        new_solution = copy.copy(current_solution)
        new_solution.append(alternative)
        expand_solutions(word_map, remaining_words, new_solution, expanded_solution_list)


def expand_all_romanization_solutions(word_map, word_list):
    expanded_solution_list = []
    solutions = get_romanization_solutions(word_map, word_list)
    expand_solutions(word_map, solutions, [], expanded_solution_list)

    # apply tone change logic
    expanded_solution_list = [logic.apply_pinyin_tone_change(word_list, solution) for solution in expanded_solution_list]

    return expanded_solution_list


def render_word(word, tone_numbers, spaces): 
    join_syllables_character = ''
    if spaces:
        join_syllables_character = ' '        
    if tone_numbers:
        rendered_list = [syllable.render_tone_number() for syllable in word]
    else:
        rendered_list = [syllable.render_tone_mark() for syllable in word]
    return join_syllables_character.join(rendered_list)

def render_solution(solution, tone_numbers, spaces):
    return ' '.join([render_word(word, tone_numbers, spaces) for word in solution])

def render_all_romanization_solutions(word_map, word_list, tone_numbers, spaces):
    expanded_solution_list = expand_all_romanization_solutions(word_map, word_list)
    return [render_solution(solution, tone_numbers, spaces) for solution in expanded_solution_list]

def render_single_solution(word_map, word_list, tone_numbers, spaces):
    output = ''
    character_spacing = ''
    word_spacing = ' '
    if spaces:
        character_spacing = ' '
    rendered_word_list = []
    for word in word_list:
        entry = word_map.get(word, None)
        if entry != None:
            logger.debug(f'located {word} as word')
            rendered_word_list.append(render_word(entry[0].syllables, tone_numbers, spaces))
        else:
            logger.debug(f'breaking down {word} into characters')
            syllable_list = []
            for character in list(word):
                entry = word_map.get(character, None)
                if entry != None:
                    syllable = entry[0].syllables[0]
                    syllable_list.append(syllable)
                else:
                    # implement pass through syllable here
                    syllable = syllables.PassThroughSyllable(character)
                    syllable_list.append(syllable)
            # render syllable_list to text
            if tone_numbers:
                rendered_word = character_spacing.join([syllable.render_tone_number() for syllable in syllable_list])
            else:
                rendered_word = character_spacing.join([syllable.render_tone_mark() for syllable in syllable_list])
            rendered_word_list.append(rendered_word)
    
    rendered_solution = word_spacing.join(rendered_word_list)
    return [rendered_solution]

def tokenize_to_word_list(word_map, text):
    word_list = tokenize(text)
    word_list = improve_tokenization(word_map, word_list)
    return word_list

def convert_to_romanization(word_map, text, tone_numbers, spaces):
    solution_list = []
    word_list = tokenize_to_word_list(word_map, text)
    logger.debug(f'word_list length: {len(word_list)}')
    if len(word_list) > constants.MULTI_SOLUTION_MAX_WORD_COUNT:
        return render_single_solution(word_map, word_list, tone_numbers, spaces)
    else:
        return render_all_romanization_solutions(word_map, word_list, tone_numbers, spaces)

def convert_pinyin_single_solution(data, text, tone_numbers, spaces):
    word_map = data.pinyin_map
    word_list = tokenize_to_word_list(word_map, text)
    logger.debug(f'word_list: {pprint.pformat(word_list)}')
    return render_single_solution(word_map, word_list, tone_numbers, spaces)

def convert_pinyin(data, text, tone_numbers, spaces):
    return convert_to_romanization(data.pinyin_map, text, tone_numbers, spaces)

def convert_jyutping(data, text, tone_numbers, spaces):
    return convert_to_romanization(data.jyutping_map, text, tone_numbers, spaces)

def tokenize(text):
    seg_list = jieba.cut(text)
    word_list = list(seg_list)
    return word_list

def improve_tokenization(word_map, word_list):
    # sometimes jieba will not tokenize certain words like 投资银行, however the character-by-character
    # pinyin conversion renders the last character as xing2. a second pass to try to further break down
    # if the word is not found in the pinyin dictionary gives a better chance to find a good match.
    # for example with 投资银行, breaking down as 投资, 银行 is better

    iterations = 0

    final_word_list = []
    for word in word_list:
        if len(word) == 1 or word in word_map:
            final_word_list.append(word)
        else:
            logger.debug(f'attempting improved tokenization for {word}')
            word_breakdown = []
            word_remaining_chars = word
            found_larger_matches = 0
            continue_iteration = True
            while continue_iteration:
                iterations += 1
                assert iterations < 1000, f'infinite loop while running improve_tokenization for {word_list}'

                logger.debug(f'word_remaining_chars: [{word_remaining_chars}]')
                # try to identify sub-words which are present in the map
                found_matches = False
                for i in range(len(word_remaining_chars) - 1, 1, -1):
                    logger.debug(f'looking for word of length {i}')
                    sub_word = word_remaining_chars[0:i]
                    if sub_word in word_map:
                        logger.debug(f'found match for {sub_word}')
                        found_matches = True
                        word_breakdown.append(sub_word) 
                        word_remaining_chars = word_remaining_chars[i:]
                        found_larger_matches += 1
                        break
                logger.debug(f'found_matches: {found_matches}')
                if found_matches == False:
                    continue_iteration = False
                #continue_iteration = 
                if len(word_remaining_chars) <= 2:
                    continue_iteration = False

            if len(word_remaining_chars) > 0:
                word_breakdown.append(word_remaining_chars)
            
            # did we find larger matches ?
            if found_larger_matches > 0:
                # then use the new breakdown
                final_word_list.extend(word_breakdown)
            else:
                # use original word
                final_word_list.append(word)
                

    return final_word_list