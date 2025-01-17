from app.models import db, Like, environment, SCHEMA
from sqlalchemy.sql import text


def seed_likes():
    like_1 = Like(
        user_id=1, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_2 = Like(
        user_id=2, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_3 = Like(
        user_id=3, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_4 = Like(
        user_id=4, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_5 = Like(
        user_id=5, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_6 = Like(
        user_id=6, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_7 = Like(
        user_id=4, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_8 = Like(
        user_id=5, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_9 = Like(
        user_id=6, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_11 = Like(
        user_id=1, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_12 = Like(
        user_id=2, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_13 = Like(
        user_id=3, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_14 = Like(
        user_id=4, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_15 = Like(
        user_id=5, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_16 = Like(
        user_id=6, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_17 = Like(
        user_id=1, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_18 = Like(
        user_id=2, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_19 = Like(
        user_id=3, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_21 = Like(
        user_id=1, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_22 = Like(
        user_id=2, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_23 = Like(
        user_id=3, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_24 = Like(
        user_id=4, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_25 = Like(
        user_id=5, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_26 = Like(
        user_id=6, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_27 = Like(
        user_id=4, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_28 = Like(
        user_id=5, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_29 = Like(
        user_id=6, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_31 = Like(
        user_id=1, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_32 = Like(
        user_id=2, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_33 = Like(
        user_id=3, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_34 = Like(
        user_id=4, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_35 = Like(
        user_id=5, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_36 = Like(
        user_id=6, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_37 = Like(
        user_id=4, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_38 = Like(
        user_id=5, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_39 = Like(
        user_id=6, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_40 = Like(
        user_id=2, player_id='4e152a06-673e-4701-b115-aa7e2cd00d2d')
    like_41 = Like(
        user_id=3, player_id='5e86a9c3-b4d0-4fe1-a551-acd83e5d60eb')
    like_42 = Like(
        user_id=4, player_id='8d3edba8-9004-4199-9328-cc2208e8b0d3')
    like_43 = Like(
        user_id=5, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_44 = Like(
        user_id=6, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_45 = Like(
        user_id=2, player_id='254e42d7-df01-4c68-9264-bca06c83c2c1')
    like_46 = Like(
        user_id=3, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_47 = Like(
        user_id=4, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_48 = Like(
        user_id=5, player_id='5382cf43-3a79-4a5a-a7fd-153906fe65dd')
    like_49 = Like(
        user_id=6, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc')
    like_50 = Like(
        user_id=2, player_id='5cc51c05-06f5-4ae4-89a4-1d329fbbcdfb')
    like_51 = Like(
        user_id=3, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6')
    like_52 = Like(
        user_id=4, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6')
    like_53 = Like(
        user_id=2, player_id='8d3edba8-9004-4199-9328-cc2208e8b0d3')
    like_54 = Like(
        user_id=3, player_id='8d3edba8-9004-4199-9328-cc2208e8b0d3')
    like_55 = Like(
        user_id=6, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6')
    like_56 = Like(
        user_id=1, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_61 = Like(
        user_id=7, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_62 = Like(
        user_id=8, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_63 = Like(
        user_id=9, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_64 = Like(
        user_id=10, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_65 = Like(
        user_id=11, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_66 = Like(
        user_id=12, player_id='d2ee92e9-3e72-45eb-b156-2dc5adc1e6f7')
    like_67 = Like(
        user_id=13, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_68 = Like(
        user_id=14, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_69 = Like(
        user_id=15, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_70 = Like(
        user_id=16, player_id='5382cf43-3a79-4a5a-a7fd-153906fe65dd')
    like_71 = Like(
        user_id=17, player_id='5382cf43-3a79-4a5a-a7fd-153906fe65dd')
    like_72 = Like(
        user_id=18, player_id='5382cf43-3a79-4a5a-a7fd-153906fe65dd')
    like_73 = Like(
        user_id=19, player_id='5382cf43-3a79-4a5a-a7fd-153906fe65dd')
    like_74 = Like(
        user_id=20, player_id='5382cf43-3a79-4a5a-a7fd-153906fe65dd')
    like_75 = Like(
        user_id=21, player_id='5382cf43-3a79-4a5a-a7fd-153906fe65dd')
    like_76 = Like(
        user_id=9, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_77 = Like(
        user_id=7, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_78 = Like(
        user_id=8, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_79 = Like(
        user_id=9, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_80 = Like(
        user_id=16, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_81 = Like(
        user_id=17, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_82 = Like(
        user_id=18, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_83 = Like(
        user_id=19, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_84 = Like(
        user_id=20, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_85 = Like(
        user_id=21, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_86 = Like(
        user_id=10, player_id='8ec91366-faea-4196-bbfd-b8fab7434795')
    like_87 = Like(
        user_id=11, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_88 = Like(
        user_id=12, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_89 = Like(
        user_id=13, player_id='ea8826b8-1f76-4eab-b61e-ffcb176880f3')
    like_91 = Like(
        user_id=7, player_id='4e152a06-673e-4701-b115-aa7e2cd00d2d')
    like_92 = Like(
        user_id=8, player_id='4e152a06-673e-4701-b115-aa7e2cd00d2d')
    like_93 = Like(
        user_id=9, player_id='4e152a06-673e-4701-b115-aa7e2cd00d2d')
    like_94 = Like(
        user_id=10, player_id='4e152a06-673e-4701-b115-aa7e2cd00d2d')
    like_95 = Like(
        user_id=11, player_id='4e152a06-673e-4701-b115-aa7e2cd00d2d')
    like_96 = Like(
        user_id=12, player_id='4e152a06-673e-4701-b115-aa7e2cd00d2d')
    like_97 = Like(
        user_id=13, player_id='254e42d7-df01-4c68-9264-bca06c83c2c1')
    like_98 = Like(
        user_id=14, player_id='254e42d7-df01-4c68-9264-bca06c83c2c1')
    like_99 = Like(
        user_id=15, player_id='254e42d7-df01-4c68-9264-bca06c83c2c1')
    like_100 = Like(
        user_id=16, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_101 = Like(
        user_id=17, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_102 = Like(
        user_id=18, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_103 = Like(
        user_id=19, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_104 = Like(
        user_id=20, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_105 = Like(
        user_id=21, player_id='6c60282d-165a-4cba-8e5a-4f2d9d4c5905')
    like_106 = Like(
        user_id=9, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_107 = Like(
        user_id=7, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_108 = Like(
        user_id=8, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_109 = Like(
        user_id=9, player_id='53f2fa48-e61b-49fb-843d-8a3e872257eb')
    like_110 = Like(
        user_id=16, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_111 = Like(
        user_id=17, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_112 = Like(
        user_id=18, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_113 = Like(
        user_id=19, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_114 = Like(
        user_id=20, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_115 = Like(
        user_id=21, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_116 = Like(
        user_id=10, player_id='0afbe608-940a-4d5d-a1f7-468718c67d91')
    like_117 = Like(
        user_id=11, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6')
    like_118 = Like(
        user_id=12, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6')
    like_119 = Like(
        user_id=13, player_id='31baa84f-c759-4f92-8e1f-a92305ade3d6')
    like_120 = Like(
        user_id=16, player_id='75fc46eb-71d8-4d1a-984f-3747ccd7a4c9')
    like_121 = Like(
        user_id=17, player_id='75fc46eb-71d8-4d1a-984f-3747ccd7a4c9')
    like_122 = Like(
        user_id=18, player_id='75fc46eb-71d8-4d1a-984f-3747ccd7a4c9')
    like_123 = Like(
        user_id=19, player_id='75fc46eb-71d8-4d1a-984f-3747ccd7a4c9')
    like_124 = Like(
        user_id=20, player_id='75fc46eb-71d8-4d1a-984f-3747ccd7a4c9')
    like_125 = Like(
        user_id=21, player_id='75fc46eb-71d8-4d1a-984f-3747ccd7a4c9')
    like_126 = Like(
        user_id=9, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_127 = Like(
        user_id=7, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_128 = Like(
        user_id=8, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_129 = Like(
        user_id=9, player_id='d9ea4a8f-ff51-408d-b518-980efc2a35a1')
    like_130 = Like(
        user_id=16, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_131 = Like(
        user_id=17, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_132 = Like(
        user_id=18, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_133 = Like(
        user_id=19, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_134 = Like(
        user_id=20, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_135 = Like(
        user_id=21, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_136 = Like(
        user_id=10, player_id='f2625432-3903-4f90-9b0b-2e4f63856bb0')
    like_137 = Like(
        user_id=11, player_id='5e86a9c3-b4d0-4fe1-a551-acd83e5d60eb')
    like_138 = Like(
        user_id=12, player_id='5e86a9c3-b4d0-4fe1-a551-acd83e5d60eb')
    like_139 = Like(
        user_id=13, player_id='5e86a9c3-b4d0-4fe1-a551-acd83e5d60eb')
    like_140 = Like(
        user_id=16, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_141 = Like(
        user_id=17, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_142 = Like(
        user_id=18, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_143 = Like(
        user_id=19, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_144 = Like(
        user_id=20, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_145 = Like(
        user_id=21, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_146 = Like(
        user_id=10, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_147 = Like(
        user_id=7, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_148 = Like(
        user_id=8, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_149 = Like(
        user_id=9, player_id='98e2cdeb-69dc-499c-a853-84c32c714924')
    like_150 = Like(
        user_id=16, player_id='eb91a4c8-1a8a-46bf-86e6-e16950b67ef6')
    like_151 = Like(
        user_id=17, player_id='eb91a4c8-1a8a-46bf-86e6-e16950b67ef6')
    like_152 = Like(
        user_id=18, player_id='eb91a4c8-1a8a-46bf-86e6-e16950b67ef6')
    like_153 = Like(
        user_id=19, player_id='eb91a4c8-1a8a-46bf-86e6-e16950b67ef6')
    like_154 = Like(
        user_id=20, player_id='eb91a4c8-1a8a-46bf-86e6-e16950b67ef6')
    like_155 = Like(
        user_id=21, player_id='eb91a4c8-1a8a-46bf-86e6-e16950b67ef6')
    like_156 = Like(
        user_id=9, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc')
    like_157 = Like(
        user_id=7, player_id='cfc1e41b-74ab-45ee-8132-aaf9ca7f8163')
    like_158 = Like(
        user_id=8, player_id='cfc1e41b-74ab-45ee-8132-aaf9ca7f8163')
    like_159 = Like(
        user_id=9, player_id='cfc1e41b-74ab-45ee-8132-aaf9ca7f8163')
    like_160 = Like(
        user_id=16, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc')
    like_161 = Like(
        user_id=17, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc')
    like_162 = Like(
        user_id=18, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc')
    like_163 = Like(
        user_id=19, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc')
    like_164 = Like(
        user_id=20, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc')
    like_165 = Like(
        user_id=21, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc')
    like_166 = Like(
        user_id=10, player_id='a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc')
    like_167 = Like(
        user_id=11, player_id='c12fb587-fc86-471c-8a84-19caf31325ce')
    like_168 = Like(
        user_id=12, player_id='c12fb587-fc86-471c-8a84-19caf31325ce')
    like_169 = Like(
        user_id=13, player_id='c12fb587-fc86-471c-8a84-19caf31325ce')

    db.session.add(like_1)
    db.session.add(like_2)
    db.session.add(like_3)
    db.session.add(like_4)
    db.session.add(like_5)
    db.session.add(like_6)
    db.session.add(like_7)
    db.session.add(like_8)
    db.session.add(like_9)
    db.session.add(like_11)
    db.session.add(like_12)
    db.session.add(like_13)
    db.session.add(like_14)
    db.session.add(like_15)
    db.session.add(like_16)
    db.session.add(like_17)
    db.session.add(like_18)
    db.session.add(like_19)
    db.session.add(like_21)
    db.session.add(like_22)
    db.session.add(like_23)
    db.session.add(like_24)
    db.session.add(like_25)
    db.session.add(like_26)
    db.session.add(like_27)
    db.session.add(like_28)
    db.session.add(like_29)
    db.session.add(like_31)
    db.session.add(like_32)
    db.session.add(like_33)
    db.session.add(like_34)
    db.session.add(like_35)
    db.session.add(like_36)
    db.session.add(like_37)
    db.session.add(like_38)
    db.session.add(like_39)
    db.session.add(like_40)
    db.session.add(like_41)
    db.session.add(like_42)
    db.session.add(like_43)
    db.session.add(like_44)
    db.session.add(like_45)
    db.session.add(like_46)
    db.session.add(like_47)
    db.session.add(like_48)
    db.session.add(like_49)
    db.session.add(like_50)
    db.session.add(like_51)
    db.session.add(like_52)
    db.session.add(like_53)
    db.session.add(like_54)
    db.session.add(like_55)
    db.session.add(like_56)
    db.session.add(like_61)
    db.session.add(like_62)
    db.session.add(like_63)
    db.session.add(like_64)
    db.session.add(like_65)
    db.session.add(like_66)
    db.session.add(like_67)
    db.session.add(like_68)
    db.session.add(like_69)
    db.session.add(like_70)    
    db.session.add(like_71)
    db.session.add(like_72)
    db.session.add(like_73)
    db.session.add(like_74)
    db.session.add(like_75)
    db.session.add(like_76)
    db.session.add(like_77)
    db.session.add(like_78)
    db.session.add(like_79)
    db.session.add(like_80)
    db.session.add(like_81)
    db.session.add(like_82)
    db.session.add(like_83)
    db.session.add(like_84)
    db.session.add(like_85)
    db.session.add(like_86)
    db.session.add(like_87)
    db.session.add(like_88)
    db.session.add(like_89)
    db.session.add(like_91)
    db.session.add(like_92)
    db.session.add(like_93)
    db.session.add(like_94)
    db.session.add(like_95)
    db.session.add(like_96)
    db.session.add(like_97)
    db.session.add(like_98)
    db.session.add(like_99)
    db.session.add(like_100)    
    db.session.add(like_101)
    db.session.add(like_102)
    db.session.add(like_103)
    db.session.add(like_104)
    db.session.add(like_105)
    db.session.add(like_106)
    db.session.add(like_107)
    db.session.add(like_108)
    db.session.add(like_109)
    db.session.add(like_110)
    db.session.add(like_111)
    db.session.add(like_112)
    db.session.add(like_113)
    db.session.add(like_114)
    db.session.add(like_115)
    db.session.add(like_116)
    db.session.add(like_117)
    db.session.add(like_118)
    db.session.add(like_119)
    db.session.add(like_120)    
    db.session.add(like_121)
    db.session.add(like_122)
    db.session.add(like_123)
    db.session.add(like_124)
    db.session.add(like_125)
    db.session.add(like_126)
    db.session.add(like_127)
    db.session.add(like_128)
    db.session.add(like_129)
    db.session.add(like_130)
    db.session.add(like_131)
    db.session.add(like_132)
    db.session.add(like_133)
    db.session.add(like_134)
    db.session.add(like_135)
    db.session.add(like_136)
    db.session.add(like_137)
    db.session.add(like_138)
    db.session.add(like_139)
    db.session.add(like_140)
    db.session.add(like_141)
    db.session.add(like_142)
    db.session.add(like_143)
    db.session.add(like_144)
    db.session.add(like_145)
    db.session.add(like_146)
    db.session.add(like_147)
    db.session.add(like_148)
    db.session.add(like_149)
    db.session.add(like_150)
    db.session.add(like_151)
    db.session.add(like_152)
    db.session.add(like_153)
    db.session.add(like_154)
    db.session.add(like_155)
    db.session.add(like_156)
    db.session.add(like_157)
    db.session.add(like_158)
    db.session.add(like_159)
    db.session.add(like_160)
    db.session.add(like_161)
    db.session.add(like_162)
    db.session.add(like_163)
    db.session.add(like_164)
    db.session.add(like_165)
    db.session.add(like_166)
    db.session.add(like_167)
    db.session.add(like_168)
    db.session.add(like_169)
    db.session.commit()

def undo_likes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.likes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM likes"))
        
    db.session.commit