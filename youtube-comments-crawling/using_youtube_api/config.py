KEY=""
STORE_FILE_PATH= ""
PREPROCESSING_PATH=""
LOG_FILE="log.txt"

VIDEO_IDS = {
    # show
    'oh_my_girl': {
        'nonstop' : 'iDjQSdN_ig8',
        'the_fifth_season' : 'udGwca1HBM4',
        'bungee' : 'QTD_yleCK9Y',
        'closer': 'isUudT58Xfk',
    },
    'chungha': {
        'stay_tonight': 'YPFIh0dfYfw',
        'roller_coaster': '900X9fDFLc4',
        'snapping' : 'deV_DmHKwjc'
    },
    'mamamoo': {
        'spit_it_out': 'bD06B-5SsSE',
        'egotistic': 'pHtxTSiPh5I',
        'starry_night' : '0FB2EoKTK_Q'
    },
    'g_idle': {
        'oh_my_god': 'om3n2ni8luE',
        'latata': '9mQk7Evt6Vs',
        'hann' : 'OKNXn2qCEws'
    },
    'itzy': {
        'wannabe': 'fE2h3lGlOsk',
        'icy': 'zndvqTc4P9I',
        'dalla_dalla' : 'pNfTK39k55U'
    },
    'nct': {
        'ridin': 'vofjeJvRT9c',
        'boom': 'X-iJZ0gfKPo',
        'we_go_up' : 'LV1Es22E0RI'
    },
    'zico': {
        'anysong': 'UuV2BmJ1p_I',
        'icy': 'ewjucLierFc',
        'i_am_you_you_are_me' : 'obzb7nlpXZ0',
        'shes_baby': 'ohSpvSGXfhY'
    },
    'bts': {
        'on': 'mPVDGOVjRQ0',
        'dna': 'MBdVXkSdhwU',
        'boy_with_love' : 'XsX3ATc3FbA'
    },
    'winner': {
        'remember': 'NTJ8esMHW2E',
        'everyday': 'd1D1SJ-KqaQ',
        'really_really' : '4tBnF46ybZk'
    },
    'kangdaniel': {
        '2u': 'GmqfRBaJm6I',
        'what_are_you_up_to': '_-QY40Reub8',
        'touchin' : 'aSGisoCdLPc'
    },
    'in_real_life': {
        'she_do': 'TXTMIhhdRpE',
        'tonight_belongs_to_you': 'xARyV3h1SB0',
        'tatoo' : 'TqDg-PLCJiE',
        'eyes_closed': 'TU72VrQEzsA'
    },
    'prettymuch': {
        'blind': 'j4FL7CMustE',
        'teacher': 'PLyMj7k5Ths',
        'me_necesita' : 'M7j3J1sTDFc'
    },
    'onedirection': {
        'perfect': 'Ho32Oh6b4jc',
        'drag_me_down': 'Jwgf3wmiA04',
        'history' : 'yjmp8CoZBIo'
    },
    'justin_bieber': {
        'yummy': '8EJ3zbKTWQ8',
        'what_do_you_mean': 'DK_0jXPuIr0',
        'sorry' : 'fRh_vgS2dFE'
    },
    'why_dont_we': {
        'chills': 'wTdZbbx53uk',
        '8letters': 'C3DlM19x4RQ',
        'trust_fund_baby' : 'fOmhbMXY52o'
    },
    'little_mix': {
        'wasabi': 'ee5aEU4XEnc',
        'shout_out_to_my_ex': 'bFDzhKdrN9M',
        'power' : 'Dw8B1q1tKgs'
    },
    'dualipa': {
        'break_my_heart': 'Nj2U6rhnucI',
        'dont_start_now': 'oygrmJFKYZY',
        'new_rules' : 'k2qgadSvNyU'
    },
    'fifth_harmony': {
        'worth_it': 'YBHQbu5rbdQ',
        'work_from_home': '5GL9JoH4Sws',
        'dont_say_you_love_me' : 'ju_inUnrLc4'
    },
    'ariana_grande': {
        '7rings': 'QYh6mYIJG2Y',
        'no_tears_left_to_cry': 'ffxKSjUwKdU',
        'thanku_next' : 'gl1aHhXnN1k'
    },
    'doja_cat': {
        'say_so': 'pok8H_KF1FA',
        'boss_bitch': 'RsW66teC0BQ',
        'juicy' : 'YIALlhlyqO4'
    },

    # interview
    'oh_my_girl': {
        '1': 'f2vhWL_vNCU',
        '2': '6LIQHLHm-P4',
        '3' : 'Wl_bBKOY9hE'
    },
    'chungha': {
        '1': 'wTjfPwM0bds',
        '2': 'jYKnUJNIysA',
        '3' : 'xX06wyXaOMg&t=4s'
    },
    'mamamoo': {
        '1': 'bsE4Ar5VtvU',
        '2': 'HlIUt1qiqsI',
        '3' : 'iotPrvKMbSQ'
    },
    'g_idle': {
        '1': 'kMVY3GNNgBw',
        '2': 'sce5ct7nCVE',
        '3' : 'E5TMUsmCvYc'
    },
    'itzy': {
        '1': 'tPOmSygIzfs',
        '2': '2dmwbprcW1U',
        '3' : 'W377EZGx2o8'
    },
    'nct': {
        '1': 'Uy-fRAFktx0',
        '2': '-fIwav5vHRI',
        '3' : 'UbMPppUEeAQ'
    },
    'zico': {
        '1': 'O0sr-G0tfPM',
        '2': '7ppNke-rEio',
        '3' : 'jNKW6GqN-vc'
    },
    'bts': {
        '1': 'm9FxeVlDFRk',
        '2': 'NSvO7xGGk-U',
        '3' : 'GKImwhn3c_E'
    },
    'winner': {
        '1': 'yvsQrXh-VLQ',
        '2': 'exVBHqjqI8I',
        '3' : '33Lmyy6HtdY'
    },
    'kangdaniel': {
        '1': 'pE7C-tqZQok',
        '2': 'V-4UfI2wG0A',
        '3' : '7E5SkM9LwLk'
    },
    'in_real_life': {
        '1': 'y2wzgCFN5yE',
        '2': 'lbp-M-gTIXM',
        '3' : '1dV2fT2Qqkw'
    },
    'prettymuch': {
        '1': 'jl2vK4vHTUo',
        '2': 'CuAtfWI24wg',
        '3' : 'LX-3bYZe1ME'
    },
    'onedirection': {
        '1': 'pnG_VgzBpvM',
        '2': 'Rc4wF3o0ZP4',
        '3' : 'fhgfH0S_zgE'
    },
    'justin_bieber': {
        '1': 'T_fw3qNx1OM',
        '2': 'e-PZxds5yWs',
        '3' : '9wu2328g_6A'
    },
    'why_dont_we': {
        '1': 'jD9iV1x-2cE',
        '2': '3wAWMbdyP3w',
        '3' : 'Yjq3nIdt64Y'
    },
    'little_mix': {
        '1': 'jVHsXdsAO-U',
        '2': 'p09LHEdvcxo',
        '3' : '_Y13PlhYH1M'
    },
    'dualipa': {
        '1': 'gsrakIxmHEY',
        '2': 'xVoT6EZHOPE',
        '3' : 'dqdqOlL3aTQ'
    },
    'fifth_harmony': {
        '1': 'g9n0QDs2dyg',
        '2': 'e_-bHU39uiU',
        '3' : '9GpzH9n0yiY'
    },
    'ariana_grande': {
        '1': 'HqgimznGHbA',
        '2': 'fpl8v3jiuNU',
        '3' : 'lm7IUJeRFEw'
    },
    'doja_cat': {
        '1': '6HgDa0RcZ0I',
        '2': 'GVk0wkkLdv8',
        '3' : 'cHqf2M0SqFI'
    }
}