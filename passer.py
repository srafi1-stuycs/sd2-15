#! /bin/env python

# Shakil Rafi
# SoftDev2 pd7
# K15 -- Do you even list?
# 2018-04-25

UC_LETTERS = 'QWERTYUIOPASDFGHJKLZXCVBNM'
LC_LETTERS = 'qwertyuiopasdfghjklzxcvbnm'
NUMS = '1234567890'
NONALPHANUM = '.?!&#,;:-_*'

def pass_check(pword):
    includes_num = [ c in NUMS for c in pword ]
    includes_uc = [ c in UC_LETTERS for c in pword ]
    includes_lc = [ c in LC_LETTERS for c in pword ]

    has_num = False
    for c in includes_num:
        if c:
            has_num = True
            break
    has_uc = False
    for c in includes_uc:
        if c:
            has_uc = True
            break
    has_lc = False
    for c in includes_lc:
        if c:
            has_lc = True
            break
    return has_lc and has_uc and has_num

def pass_strength(pword):
    includes_num = [ c in NUMS for c in pword ]
    includes_uc = [ c in UC_LETTERS for c in pword ]
    includes_lc = [ c in LC_LETTERS for c in pword ]
    includes_nam = [ c in NONALPHANUM for c in pword ]

    num_num = 0
    for c in includes_num:
        if c:
            num_num += 1
    num_uc = 0
    for c in includes_uc:
        if c:
            num_uc += 1
    num_lc = 0
    for c in includes_lc:
        if c:
            num_lc += 1
    num_nam = 0
    for c in includes_nam:
        if c:
            num_nam += 1

    return int(num_num*0.2 + num_uc*0.3 + num_lc*0.4 + num_nam*0.7)
