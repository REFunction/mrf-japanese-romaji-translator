special_chars = '!@#$%^&*()_+~-=[]\;\',./<>?\{\}|:\"`დღ♡❣❤❥❦❧♥♩♪♫♬♭♮♯☠☤☥☦☧☨☩☪☫☬☮☭☯☸☽☾♕♚♛✙✚✛✜✝✞✟✠✡✢卍卐‱№℗℠℡℀℁℅℆⅍⌚⌛☊☎☏✁✂✃✄✆✇✈✉✍✎✏✐✑✒™©®‰§¶'+\
'♈♉♊♋♌♍♎♏♐♑♒♓↕↖↗↘↙↚↛↜↝↞↟↠↡↢↣↤↥↦↧↨↩↪↫↬⊖⊘⊙⊚⊛⊜⊝◉○◌◍◎●◐◑◒◓◔◕◖◗◦◯❍⦿⊕⊗∆⊿▲△▴▵▶▷▸▹►▻▼▽▾▿◀◁◂◃◄◅◢◣◤◥◬◭◮∇'+\
'✿҉ღ҉℘ೄζั͡ตԅ️✾ೄ೨❀҉এృةمʚΐɞʚɞﻬ๑ف๓ق⏎⇧⇪⌂⌘☢☣⌥⎋⌫ᴴᴰ_§:ºั๑৫(”ړ৫｡ﾉ♡Ծ‸♕♖♚♛♜☀☁☂☃☼☽☾♨❄❅❆★☆✦✪✫✿❀❁♥❤ღ☑✔✘ㄨ✖✉☎♂♀웃유☣☤⌘༄☯☭❧⚘✍✎✑✂✄☹☺☻☪❂☬☸♆☩◙❦☸♠♣♥♤♡❤❥❣❇❈❊✳✴✻'+\
'♔♕♖♗♘♙♚♛♜♝♞♟ϟ☀☁☂☃☄☉☼☽☾♁♨❄❅❆﹢﹣×÷±/=≌∽≦≧≒﹤﹥≈≡≠=≤≥<>≮≯∷∶∫∮∝∞∧∨∑∏∪∩∈∵∴⊥∥∠⌒⊙√∟⊿㏒㏑%‰⅟½⅓⅕⅙⅛⅔⅖⅚⅜¾⅗⅝⅞⅘≂≃≄≅≆≇≈≉≊≋≌≍≎≏≐≑≒≓≔≕≖≗≘≙≚≛≜≝≞≟≠≡≢≣≤≥≦≧≨≩⊰⊱⋛⋚∫∬∭∮∯∰∱∲∳%℅‰‱øØπ'+\
'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя₠₡₢₣₤₥₦₧₨₩₪₫₭₮₯₰₱₲₳₴₵'+\
'✁✂✃✄✆✇✈✉✌✍✎✏✐✑✒✓✔✕✖✗✘✙✚✛✜✝✞✟✠✡✢✣✤✥✦✧✩✪✫✬✭✮✯✰✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋❍❏❐❑❒❖❘❙❚❛❜❝❞❡❢'+\
'❣❤❥❦❧❶❷❸❹❺❻❼❽❾❿➀➁➂➃➄➅➆➇➈➉➊➋➌➍➎➏➐➑➒➓➔➘➙➚➛➜➝➞➟➠➡➢➣➤➥➦➧➨➩➪➫➬➭➮➯➱➲➳➴➵➶➷➸➹➺➻➼➽➾oò'+\
'`ˊᐟ‐‑‒―⁃≣⋐⋑⋒⋓⌒⌜⌝⌞⌟⎯─━│┃┄┅┆┇┈┉┊┋┌┍┎┏┐┑┒┓└└┕┖┗┘┙┚┛├├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋╌╍╎╏══║╒╓╔╔╔╕╕╖╖╗╗╘╙╚╚╛╛╜╜╝╝╞╟╟╠╡╡╢╢╣╣╤╤╥╥╦╦╧╧╨╨╩╩╪╪╫╬╬╭╮╯╰╱╲╳╴╵╶╷╸╹╺╻╼╽╾╿▏▕◜◝◞◟◠◡☰☱☲☳☴☵☶☷✕≡⌈⌊—⌉⌋'+\
'℃℉㎎㎏㎜㎝㎞㎡㏄㏎㏑㏒㏕¹²³⁰ⁱ⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₔąčĤħĩŇŘŤŴŽ⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭'+\
'⒮⒯⒰⒱⒲⒳⒴⒵ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯ'+\
'ＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚáâæàåãäçéêèðëíîìïñóôòøõößþúûùüýÿ'+\
'˙‥‧‵‵❛❜❝❞、。〃「」『』〝〞︰︰﹁﹂﹃﹄﹐﹒﹔﹔﹕！＃＄％＆＊，．：；？＠～•…¿“‘·′”'+\
'〈〈〉《》「」『』【】〔〕︵︶︷︸︹︺︻︼︽︽︾︿﹀﹁﹁﹂﹃﹄﹙﹙﹚﹛﹜﹝﹞﹤﹥（）＜＞｛｛｝'+\
'₮৲৳௹฿៛₠₡₢₣₤₥₦₧₨₩₪₫₭₯₰₱₲₳₴₵￥﷼¢¤€ƒ£¥'