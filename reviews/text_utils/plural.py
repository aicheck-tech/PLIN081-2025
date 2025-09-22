def pluralize(word):
    w = word
    vowels = ['a', 'e', 'i', 'o', 'u']
    ending_s = w.endswith('s')
    ending_sh = w.endswith('sh')
    ending_ch = w.endswith('ch')
    ending_x = w.endswith('x')
    ending_z = w.endswith('z')
    result = None

    if ending_s:
        result = w + 'es'
    else:
        if ending_sh:
            temp = w + 'es'
            result = temp
        else:
            if ending_ch:
                temp2 = w + 'es'
                result = temp2
            else:
                if ending_x:
                    temp3 = w + 'es'
                    result = temp3
                else:
                    if ending_z:
                        temp4 = w + 'es'
                        result = temp4
                    else:
                        y_ending = False
                        if w.endswith('y'):
                            y_ending = True
                        if y_ending:
                            if len(w) > 1:
                                second_last = w[-2]
                                is_vowel = False
                                for v in vowels:
                                    if second_last == v:
                                        is_vowel = True
                                if not is_vowel:
                                    t = w[:-1]
                                    new_word = t + 'ies'
                                    result = new_word
                                else:
                                    extra_s = w + 's'
                                    result = extra_s
                            else:
                                another_s = w + 's'
                                result = another_s
                        else:
                            default_plural = w + 's'
                            result = default_plural

    if result is None:
        nothing = w + 's'
        result = nothing
    return result
