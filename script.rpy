# 备注：请看备注

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
# 虽然目前图片还不全()，但我先声明好角色，后续优化时方便添加
define zhangyouxi = Character("张有喜", color="#ffffff")
define lidaniang = Character("李大娘", color="#ffffff")
define wangxiufeng = Character("王秀风", color="#ffffff")
define lisan = Character("李三", color="#ffffff")
define zhaohanlie = Character("赵汉烈", color="#ffffff")
define liuhu = Character("刘虎", color="#ffffff")
define village_head = Character("村长", color="#ffffff")
define villager_a = Character("中年村民A", color="#ffffff")
define villager_b = Character("青年村民B", color="#ffffff")
define villager_c = Character("村民C", color="#ffffff")
define villager_d = Character("村民D", color="#ffffff")
define japanese_soldier_a = Character("日本人A", color="#ffffff")
define japanese_soldier_b = Character("日本人B", color="#ffffff")
define japanese_soldier_c = Character("日本人C", color="#ffffff")
define cuntian = Character("村田", color="#ffffff")
define guitian = Character("龟田", color="#ffffff") 
define child = Character("孩子", color="#ffffff")
define self_defence_team_member_a = Character("自卫队青年A", color="#ffffff")
define self_defence_team_member_b = Character("自卫队青年B", color="#ffffff")
define soldier = Character("士兵", color="#ffffff")
# 哎哎上面这里我看着是得有多个村民和士兵的图片，如果提供了材料就再加上

# ε=(´ο｀*)))唉定义图片路径烦死了，弄了半天，而且图片命名的时候带括号和冒号也不合语法
# 如果还发现哪里含有特殊字符，一律用下划线代替
image familiar people_1 = "images/familiar people-1.png"
# 读到结尾处，意识到后面_2~_7是隶属于familiar people的
image _2 = "images/-2.png"
image _3 = "images/-3.png"
image _4 = "images/-4.png"
image _5 = "images/-5.png"
image _6 = "images/-6.png"
image _7 = "images/-7.png"
image 1_bg1_1 = "images/1-bg1-1.png"
image 1_bg1_2 = "images/1-bg1-2.png"
image 1_bg2_1 = "images/1-bg2-1.png"
image 1_bg2_2 = "images/1-bg2-2.png"
image 1_bg2_3 = "images/1-bg2-3.png"
image 1_bg3_1 = "images/1-bg3-1.png"
image 1_bg3_2 = "images/1-bg3-2.png"
image 1_bg3_3 = "images/1-bg3-3.png"
image 1_bg3_4_home of lidaniang_bg = "images/1-bg3-4(home of wangdaniang_bg).png"
image 2_bg4_1_the village_bg = "images/2-bg4-1(the village_bg).png"
image 2_bg5_9_on the mountain_bg = "images/2-bg5&9(on the mountain_bg).png"
image 2_bg6_1 = "images/2-bg6-1.png"
image 2_bg7_1 = "images/2-bg7-1.png"
image 2_bg8_10_home of the village head_bg = "images/2-bg8&10(home of the village head_bg).png"
image 2_shot3 = "images/2-shot3.png"
image 2_shot4 = "images/2-shot4.png"
image Japanese devils go die_1 = "images/Japanese devils go die-1.png"
image Japanese devils go die_2 = "images/Japanese devils go die-2.png"
image 3_shot9 = "images/3-shot9.png"
image 3_shot11 = "images/3-shot11.png"
image 4_4 = "images/4-4.png"
image 4_5 = "images/4-5.png"
image 4_6 = "images/4-6.png"
image 4_7 = "images/4-7.png"
image 4_8 = "images/4-8.png"
image 4_9 = "images/4-9.png"
image 4_12 = "images/4-12.png"
image 4_13 = "images/4-13.png"
image 4_13_ = "images/4-13().png"
image 4_14 = "images/4-14.png"
image 4_15 = "images/4-15.png"
image 4_16 = "images/4-16.png"
image final_cg = "images/final_cg.png"

# 定义音效路径,示例audio blahblah = "sounds/blahblah.wav"
# audio = "sounds/.wav"

# 作一个声明：场景内背景切换我使用的都是with dissolve
# 所有的停顿我都用的2s，后面看不合适再调整

# 游戏在此开始。
label start:

    # 第一章：逃亡与收留

    # 场景1：逃亡路上
    scene 1_bg1_1 with dissolve  # 1-场景1-1
    play music train_sound

    scene 1_bg1_2 with dissolve  # 1-场景1-2

    # 场景2：回忆与现实
    scene 1_bg1_2 with dissolve
    play music wind_sound

    # 场景3：遇救
    scene 1_bg3_1 with dissolve
    show lidaniang at left with dissolve
    lidaniang "（惊喜，停下手中动作，直起身子）大壮，你终于醒了！（脸上皱纹舒展开，眼中满是关切）"
    zhangyouxi "（一脸茫然，微微皱眉）我不叫大壮啊，大壮是谁？"
    lidaniang "（微微一怔，眼神闪过一丝落寞）你这孩子糊涂了，连你娘都认不出来了？没事，等一会我用磨出来的玉米面给你蒸窝头吃！（勉强挤出笑容）"
    zhangyouxi "（有些局促，搓着手）大娘你误会了，我叫张有喜，日本人拆了我们村子，我逃亡到这来的。"
    lidaniang "（愣住，手中动作停下，眼中泛起泪花）我知道你不是我的孩子。但是还是不自觉就……唉……没关系，这顿窝窝我请你吃，可怜的孩子。"
    zhangyouxi "（不好意思，赶紧走上前）谢谢大娘，那个，我帮您磨吧。"
    lidaniang "（带着泪的微笑，点点头）咱们一块来吧，大壮还在的时候我们经常一块磨。"
    play sound mill_turning_sound
    play sound wind_sound
    play sound dog_barking_sound

    # 第二章：村庄生活

    # 场景4：村庄现状
    scene 2_bg4_1_village_bg with dissolve
    villager_a "（无奈地叹气）等到来年开春，我就收拾着逃到山东去，这日子怎么过？"
    villager_b "（焦急地）唉，我娘腿脚不利索，想走也走不掉。那个，木生叔，能不能借我家一点粮食，我家快断粮了。"
    villager_a "（面露难色）我家日子也紧得很啊，还有俩小孩要喂，自己吃都快不够了，拿不出来了。"
    liuhu "（喘着粗气，急切地）我……我看见有一队日本人……往你们村子这边来了……约莫这有十五六人，要再来抢粮食……他们一看就不熟……山上，大概……五六天后就要到了……你们……你们快准备逃吧。"
    play sound wind_sound
    play sound villagers_talking_sound

    # 场景5：结识王秀风
    scene 2_bg5_1_forest with dissolve
    show zhangyouxi at right with dissolve
    show wangxiufeng at left with dissolve
    zhangyouxi "（疑惑）那个，你跟我做什么。"
    wangxiufeng "（有些慌张，眼神闪躲）我，我是来帮忙的！你不是要给李大娘和村长砍柴火吗，我也来帮忙！"
    zhangyouxi "（上下打量）奇怪，我怎么没见过你呢？你叫啥名字？"
    wangxiufeng "（顿了顿）我叫……额，我叫王秀风，村西头王老汉家的儿子，你在东头住，没见过我正常。"
    zhangyouxi "太好了，你砍东边的，我砍北边的吧。"
    wangxiufeng "（小声）我砍得慢，你别笑话我。"
    zhangyouxi "（安慰）好了，野猪被赶跑了。秀风兄弟，野猪这样一吓就跑了，有啥可怕的。"
    wangxiufeng "（脸红，低头）那边是我砍的柴火，你先拿着回去吧，我等会再走。"
    zhangyouxi "（皱眉，看着她的脚）这不行，你这走不了了，又遇见个野猪咋办？柴火哪有你重要？"
    zhangyouxi "（背起王秀风后，身体一僵，意识到不对）额，不好意思了。"
    wangxiufeng "（沉默，脸更红了，轻轻摇头）没……没关系。"
    play sound pig_roaring_sound
    play sound footsteps_sound
    play sound wind_sound
    play sound wangxiufeng_scream_sound

    # 场景6：遇虎被救
    scene 2_bg6_1_snowy_forest with dissolve
    show zhangyouxi at right with dissolve
    show wangxiufeng at left with dissolve
    wangxiufeng "（轻声，带着一丝恐惧）给你添了好多麻烦。"
    zhangyouxi "（喘着粗气）这不算啥。"
    wangxiufeng "（颤抖）你……你听到了吗？"
    zhangyouxi "（低声，紧张）要命，是老虎！"
    lisan "（大声）好了，别在那搂搂抱抱了，怪肉麻的！"
    zhangyouxi "（惊喜，看向李三）李三叔，原来是您！"
    play sound tiger_roaring_sound
    play sound wind_sound
    play sound heavy_footsteps_sound
    play sound gun_sound

    # 场景7：李三的过往
    scene 2_bg7_1_lisan_cabin with dissolve
    show lisan at center with dissolve
    wangxiufeng "（疑惑，看向李三）叔，你有这样的本事，连老虎都不怕，而且还默默守护着村子。可是，为什么之前鬼子来的时候，一面也不出来呢？"
    lisan "（放下酒碗，沉默片刻，眼神变得深沉）对不起，丫头，我那时候不能出手。东北三省几个月内全部被小日本侵占，我杀不尽侵略村子的小鬼子，一旦把事端闹大，整个村子可能会遭受灭顶之灾。（眼神中透露出无奈和不甘）"
    lisan "（指着地图，语气坚定）我一直等待着，组织一支东北人民自己的自卫部队，向日本人复仇！我以前当过东北军的步兵连长，行军打仗，要靠团结，要靠万众一心，同仇敌忾的气势！可那时的形势还不够。中国很多地方没有一个正确的党的领导，没有觉醒的思想，不敢团结起来为幸福的日子战斗！你们知道共产党吗？我曾遇到过一个，他才是一个真正的英雄，为了他说的‘人人自由平等的新中国’付出生命来。（眼中闪烁着希望的光芒）"
    play sound fire_crackling_sound
    play sound drinking_sound
    play sound occasional_cough_sound

    # 第三章：新的希望

    # 场景8：赵汉烈到来
    scene 2_bg8_10_village_head_home with dissolve
    show zhaohanlie at right with dissolve
    village_head "（微笑着介绍）这个小伙子跟你一样，不过比你早一周，沦落到这里来，被我们村子收留。"
    zhaohanlie "（拱手行礼）幸会有喜兄，在下赵汉烈。"
    village_head "（看着赵汉烈，好奇地问）看孩子你的样子不像是普通人家出来的，怎么也会这般沦落？"
    zhaohanlie "（微微皱眉，眼中闪过一丝愤怒）实不相瞒，汉烈出生在一军官世家，日本人入侵，东北军方竟然妥协不抵抗，我义愤填膺，加入了东北义勇军，自发抗日。但可惜我实战经验不足，战斗失利，逃亡到这里。"
    zhangyouxi "（热情地）汉烈哥，你有啥需要帮忙的尽管跟我说，我肯定尽全力帮助！"
    zhaohanlie "（感激地）不能太麻烦兄弟你，我被村长老人家收留，自然要帮持村长家的生活，不然良心不安。只是我自幼没做过农活，还望张兄教导。"
    play sound wind_sound
    play sound indoor_talking_sound

    # 场景9：组建义勇军
    scene 2_bg4_1_village_bg with dissolve  # 镜头运动：场景2-4-1
    zhaohanlie "（眼神坚定，看向村庄）你看村子被日本人侵略得多么可怜，我打算在这一片地带组织抗日义勇军，大家团结起来，打鬼子，保家园。"
    zhangyouxi "（毫不犹豫，眼神同样坚定）我第一个加入，咱们一起为了‘人人平等幸福的新中国’努力吧！"
    zhaohanlie "（惊喜，紧紧握住张有喜的手）你说出了我一直想表达的话……"
    zhangyouxi "（腼腆）其实这句话是李三叔提到的一个共产党员讲的。"
    play sound wind_sound
    play sound indoor_talking_sound

    # 第四章：战争来临

    # 场景10：鬼子消息
    scene 2_bg4_1_village_bg with dissolve  # 镜头运动：场景2-4-1
    villager_a "（无奈地叹气）等到来年开春，我就收拾着逃到山东去，这日子怎么过？"
    villager_b "（焦急地）唉，我娘腿脚不利索，想走也走不掉。那个，木生叔，能不能借我家一点粮食，我家快断粮了。"
    villager_a "（面露难色）我家日子也紧得很啊，还有俩小孩要喂，自己吃都快不够了，拿不出来了。"
    liuhu "（喘着粗气，急切地）我……我看见有一队日本人……往你们村子这边来了……约莫这有十五六人，要再来抢粮食……他们一看就不熟……山上，大概……五六天后就要到了……你们……你们快准备逃吧。"
    play sound wind_sound
    play sound villagers_talking_sound
    play sound liuhu_panting_sound

    # <备战>

    # 场景1：村长家的老木屋
    # 镜头1：村长家的讨论
    scene 2_bg8_10_village_head_home with dissolve
    "村长长叹一口气"
    village_head "（皱眉）这么说的话，鬼子最快三天就要到了，对吧？"
    liuhu "哎呀！虽说这样，但也不至于三天就到吧。我估摸着，再等上四天是没什么问题的。"
    villager_b "（激动）再来三天四天有什么区别！逃不了，不是只有死吗？"
    villager_a "（激动）这些天一直下雪，大雪封山，逃？往哪逃？"
    zhaohanlie "（一直观察着其他人的表情）没法子，只有集合村里，紧急操练，把这些小鬼子端掉！"
    liuhu "（翘起二郎腿）好！不是个孬种，就该打死这伙狗娘养的！一人开一枪，这十五六个小鬼子不一会儿全没了，哈哈！"
    villager_b "（指着汉烈）汉烈，你说得轻巧，小鬼子都经过训练的，十五六个，一伙涌上来，谁挡得住那火力？这不就是相当于十几个熊进村吗？"
    villager_a "（撇过头）打我肯定不打，我现在就回家里收拾收拾，明早雪一停，我就往南逃！"
    liuhu "你这家伙刚刚有胆对我开枪，怎么就没胆跟小鬼子干一架？小鬼子来了，你家里没被抢，你家里没死人？你不会琢磨着，不跟小鬼子反着来，你……（被打断）"
    villager_a "（脸色大变，额头青筋暴起，大步走到刘虎面前，一脚冲他踹去。刘虎被连人带凳一脚蹬翻）（巨大的“砰”一声）你这没娘教的东西！"
    liuhu "（立马站起身,举起拳头要动手）你……（被青年村民拉住）"  # 我发现这里不能在青年村民后加b或B，否则括号会被识别为特殊字符
    zhaohanlie "（拉开两人）木生叔，大局为重！"
    play sound coal_lamp_burning_sound
    play sound villagers_talking_sound
    play sound villager_a_angry_sound

    # 镜头2：村长的决定
    village_head "（气沉丹田，铿锵有力）打！必须打！"
    play sound village_head_determined_sound

    # 镜头3：村长的背影
    village_head "（颤颤巍巍地起身，深一脚浅一脚地踏过天井的积雪，往茅房走去，留下矮矮的背影）"
    play sound village_head_walking_sound
    play sound snow_crunching_sound

    # 场景2：黑夜中的北山，鬼子的队伍里
    # 镜头4：鬼子的扎营
    scene 2_bg5_9_on_the_mountain_bg with dissolve
    japanese_soldier_a "村田，你的家乡，北海道那边，也是这样冷吗？"
    cuntian "没有啊，该死，怎么这么冷，我有些想回家了。"
    japanese_soldier_c "你这样的软蛋怎么混进我们部队的？不把整个中国征服，你就想逃？"
    "雪纷纷的落下,日本人B伸出手掌,看着雪花在手心融化,想起了远方的妈妈,他缓缓抬头,同一片璀璨星空下,他却远征千里,只为挣钱为妈妈买药。"
    japanese_soldier_b "(心中低语)可是……我不想杀人了，我有罪……我想回家。"
    "枪声撕裂静谧,吓了士兵们一跳。循声望去, 村田倒在血泊中，血液甚至结了冰。"
    "刚刚和村田聊天的士兵震惊地看向开枪的长官龟田"
    guitian "(凶狠)帝国的士兵，不允许这般贪生怕死！不杀戮，难道要我们自己的家被杀戮吗?"
    japanese_soldier_a "(震惊)少佐，你怎么能对同胞开枪?"
    guitian "你们，不，我们，都是帝国的兵器，如果你不接受这份荣誉，我也会对你开枪。"
    "士兵们不语,只是茫然地看着地上的尸体,血色蔓延成河,在冰面上凝固,也许下一个就是他们自己。狂风不止，像旷野上孑然的孤魂。"
    play sound wind_sound
    play sound japanese_talking_sound
    play sound gun_sound

    # 场景3：清晨村中央
    # 镜头5：紧急通知
    scene 2_bg4_1_village_bg with dissolve
    liuhu "（敲门）李大娘，有喜，村长有急事找大家，快到村中央集合！"
    "张有喜略带错愕看着这个穿黄大衣，戴鹿毡帽的小伙子。刘虎看上去也就十六七岁，他稚气中带着土气，脸颊冻得红红。"
    zhangyouxi "（开门，略带错愕）你是？"
    liuhu "俺叫……不，我叫刘虎，村长有事跟你们宣布，在村子中央。"
    zhangyouxi "你是这个村子里的人？不像。"
    liuhu "当然不是，我是来告诉你们……额，不能提前说，一会你听村长说你就知道了。"
    zhangyouxi "你也是流浪到这的？我也是。不过看你这打扮，兄弟你难道以前是土匪？"
    liuhu "（稍昂起头）你见过这么有大将风度的土匪？我可是正统军官出身。"
    zhangyouxi "（略带玩笑）和汉烈哥一样？感觉不太像啊。"
    liuhu "（轻笑一声）你……爱信不信吧。"
    play sound knocking_sound
    play sound door_opening_sound
    play sound talking_sound

    # 镜头6：村中央的集结
    scene 2_bg4_1_village_bg with dissolve
    "张有喜略带错愕看着这个穿黄大衣，戴鹿毡帽的小伙子。刘虎看上去也就十六七岁，他稚气中带着土气，脸颊冻得红红。"
    "不出意外的，有人走漏风声，有人一直都没来集合，底下逐渐议论纷纷。"
    zhaohanlie "（扯着嗓子大喊）乡亲们！安静！"
    village_head "（用最大的力气，虽气力不足，一句一顿，但力量不减）小伙子们，鬼子杀害了我们的家人，抢走了我们的粮食，我们，必须，得反抗，必须，报仇！"
    villager_b "村长，我们就拿着锄头，咋报仇！"
    village_head "（咳嗽，后继续鼓足力气）我们用猎枪！猎枪没了用锄头！锄头没了用棍子！棍子没了拿锅碗砸！锅碗没了拿拳头打，拿牙咬，拿腿踢！要是鬼子来了，我不要这把老骨头了，第一个上！"
    play sound villagers_talking_sound
    play sound village_head_speaking_sound
    play sound coughing_sound

    # 镜头7：村民的响应
    scene 2_bg4_1_village_bg with dissolve
    "众人的喧哗立刻沉寂下来，没人再嬉笑，没人再议论。村长的悲愤和决心感染了每一个人。"
    village_head "（看着一片沉默，接着说）我，没疯。你们别笑我，上次鬼子来了我是一个屁不敢放，看着儿子被打死，就那么拿枪给打死啊！"
    village_head "（激动）李服二，你爹，六十多岁的老李头，老老实实干了一辈子农活，他有什么错？凭什么被一枪打死，死得那么惨？还有王占虎，你孩子，才五岁大，你不记得是怎么死的了？王香芹，你的汉子，又是怎么死的，你也忘了？"
    "众人哑口无言，除了泪水在脸上任性"
    village_head "你们知道，我为什么要这么说吗?有十五个鬼子，就在三天后，要来抢咱们村子了！大雪封山，逃不了！逃不了啊！不打，只有死！就这么死，不行！不行！不行！"
    "村长越说越激动，尽力挺直的背因剧烈的咳嗽佝偻下去。"
    villager_b "（愤怒地）打鬼子！打鬼子！打鬼子！"
    zhaohanlie "（跟着村民一起喊）跟我一起，报仇！报仇！报仇！"
    villager_1 "我家有猎枪，要一枪打死小鬼子！"
    villager_2 "我拿斧子砍也要砍死小鬼子！"
    "人们的响应声越来越大，村子从未如此昂扬过，张有喜加入了其中。男人，女人，老人，孩子，在死亡的斧钺下竟然有着这般决绝勇魄。"
    play sound villagers_cheering_sound
    play sound village_head_speaking_sound

    # 镜头8：自卫队的成立
    scene 2_bg4_1_village_bg with dissolve
    "村子自卫队定了下来，由经过军事训练和军事理论教育的赵汉烈当总指挥，李三当教官，刘虎自告奋勇当侦查兵，张有喜也在其中，甚至，还有“王秀风”，整个自卫队，有四十二人，都是青壮年。"
    zhaohanlie "（手里拿着一根木棍，充当指挥棒）乡亲们，我们没有正规的武器，但我们的决心和勇气就是最强大的武器！"
    "他声音嘹亮，在寒冷的空气中回荡。"
    "村民们排成几列，手中拿着各种工具：锄头、镰刀、木棍，甚至还有几把锈迹斑斑的猎枪。李三站在赵汉烈身边，不时纠正着村民的动作。他的眼神坚定，仿佛回到了当年在东北军的日子。"
    lisan "嘿！小子，你这么端枪打得中谁！别害怕，把鬼子想象成一头狍子，一枪要命！就这么简单。"
    "张有喜略带错愕地看着这个穿黄大衣，戴鹿毡帽的小伙子。刘虎看上去也就十六七岁，他稚气中带着土气，脸颊冻得红红。"
    play sound villagers_training_sound
    play sound zhaohanlie_speaking_sound

    # 镜头9：刘虎的画
    scene 2_bg4_1_village_bg with dissolve
    "村西头的一个屋角，刘虎捡着一块红砖碎片，在地上画画，他还是没脱他那件黄色破旧大衣，画着山，大树，房子，鹿，枪，还有书……偶尔有孩子经过他旁边。"
    liuhu "嘿，你看我画的像不像？"
    child "你倒像个傻狍子一样。"
    liuhu "看不起我刘大将军？不服你来画一个？"
    "孩子被刘虎的凶相吓开，刘虎看着孩子走开，尴尬地摸了摸头，接着又继续自顾自地画了起来。"
    play sound liuhu_drawing_sound
    play sound child_laughing_sound

    # 镜头10：自卫队的准备
    scene 2_bg8_10_village_head_home with dissolve
    "村长家，暂时成了自卫队的指挥部。"
    lisan "不能打草惊蛇，要是鬼子有防备了，想打击他们就难了。"
    zhaohanlie "那依我之见，把北村的百姓撤到南边，空出北村，诱敌深入，来一波伏击。"
    lisan "这行不得，小伙子，你懂战术，但你不了解农民。没有杀掉几个鬼子，终究是士气不稳，有的人还是不敢打，舍不得豁出命打。咱们的战术未必服众，要是把北村撤光，那异议更大了。要知道，让农民丢掉家，在他们看来可是和叫他们丢掉命一样大的事。"
    zhaohanlie "我的确没有把这层阻力考虑在内。那要怎么？"
    zhangyouxi "（突发奇想）建一个‘假村子’，怎么样？搭几间临时茅屋，修一圈篱笆，再装点装点，看上去就跟个小村子外围一样。而且，咱们可以按照对咱们有利的地形建，提前埋伏好，敌人根本不知道咱们藏在哪！"
    lisan "（喜悦）好想法！而且可以把敌人挫在村子之外。"
    zhaohanlie "第一个问题得以解决。咱们现在就开始修起来，挖战壕，并且到时候部署二十五人左右埋伏。"
    zhaohanlie "那么，第二个问题，敌人第一波多半是不能消灭干净的。敌人势必会把村子东边或西边作为第二次进攻方位，村东和村西都要有兵力把守。而且，剩下的敌人，是最难发现，最难解决的。"
    lisan "两边都提前部七人防备。到时候依战局而定，鬼子主力去哪边，我就去追击哪边！另一边，让有喜带队去追击！"
    zhaohanlie "那么，从今天开始，组织好巡逻队，随时预备敌人来袭。"
    lisan "别看那刘虎吊儿郎当，腿脚跟野兔子一样快，而且我能感觉，这小子心里很有数。"
    play sound planning_sound
    play sound talking_sound

    # 镜头11：北村“假村子”的修建
    scene 2_bg4_1_village_bg with dissolve
    "北村“假村子”修建中，大家都卯足了劲，为与鬼子大战做准备。"
    zhangyouxi "（扭头望向秀风）你爹真的放心你来吗？"
    wangxiufeng "（一脸嫌弃）不用管那个臭酒鬼。"
    zhangyouxi "你哥哥死后，他一定很伤心吧。他怎么可能，放心你来。"
    wangxiufeng "（沉默，而后对张有喜嫣然一笑）那你担心我吗？"
    zhangyouxi "（转过头来，脸刷的一下红了）当……有些吧。"
    liuhu "（冲过来）嘿，有喜！你偷懒被我抓着了！（他的大鹿皮毡帽随脑袋摇晃着）"
    "两人相视一笑，各自继续挥动手中的铲子……"
    play sound building_sound
    play sound talking_sound
    play sound laughing_sound

    # 战争
    # 镜头1：自卫队的准备
    scene 2_bg4_1_village_bg with dissolve
    "一天过去，两天过去，村子平安无事，这两天也都是晴天。第三天到来，阴霾遮蔽天空，但雪迟迟未落。"
    "而刘虎带着两个敏捷的自卫队成员，在北边山林侦查鬼子队伍的踪迹，他们是掌握先机的关键。"
    lisan "大家注意，鬼子随时可能到来，保持警惕！"
    zhangyouxi "明白，我们会小心的。"
    play sound wind_sound
    play sound villagers_readying_sound

    # 镜头2：刘虎的侦查
    scene 2_bg5_9_on_the_mountain_bg with dissolve
    "中午，北山，小雪。"
    liuhu "（半开玩笑）哈哈，兴许鬼子绕道去别处了呢？退而……对，退而求其次！寇……对，寇贼遇大寒，道中饥寒死伤过半，驾马回逃！"
    self_defence_team_member_a "虎子，别瞎想了，注意观察。"
    self_defence_team_member_b "往北继续上山走吧，雪会越下越大的。"
    play sound wind_sound
    play sound footsteps_sound

    # 镜头3：发现敌人
    scene 2_bg5_9_on_the_mountain_bg with dissolve
    "枪声！刘虎心头一颤。"
    "声音从刘虎一行人东北侧传来，敌人已经到来。刘虎按住两个队友，自己一个人上前去勘探。"
    "越过雪坡，蜿蜒着上山，约莫走了七八百步，眼前是一队穿军服的士兵在一片林间空地烤着刚射杀的鹿。刘虎躲在正西侧的一棵巨型美人松后，竭尽全力压住呼吸。他趴下，扒开枯枝丛，偷偷看着鬼子们的状态。"
    liuhu "（自言自语）一共十四个，装备精良，有盒子枪，三八式步枪，还有九七式手雷。得赶紧通知大家。"
    "日本士兵拿刺刀炙烤着鹿肉，因风雪中的长时间行军他们折损了几名同伴，但这是最无关紧要的。粮食不够，只能靠运气好遇到猎物打猎。此时这个位置，他们已经能从北边山坡眺望到村子，欲望之火在暴虐的信仰中熊熊燃烧。屠杀，粮食，美酒，女人，金钱，多么多的乐趣，只要扣动手里的扳机就能拿到，只要模仿狮虎的凶狠就能征服，只要听从伟大的指引就能化鲜血为荣光！"
    guitian "在风雪的苦难中涅槃，我们是开辟新世界的英雄！"
    play sound gun_sound
    play sound wind_sound

    # 镜头4：刘虎的逃生
    scene 2_bg5_9_on_the_mountain_bg with dissolve
    soldier "嘿，那边的枯草堆里，是张鹿皮吗？"
    "不好，要被发现了！"
    "等等，身后，身后怎么会有声音？"
    "这声音，刘虎僵硬地扭过头去，赫然一头未冬眠的巨熊正向他逼近！"
    "饥饿的巨兽，挥动着铁爪，没有阴谋可言，没有荣耀可言，不过是自然法则的镣铐下挣扎求生的普罗生命。"
    "前方，持枪的士兵正一步步举着利刃迫近。"
    "前狼后熊，绝境难逃。刘虎在这漫长的时刻，动弹不得。"
    liuhu "（心中思绪万千）阿爸说过……阿爸说过，穿上这件军大衣，要像个将军一样临危不乱。你做好牺牲的准备了吗？可是我才十七岁。我不想死。阿妈做的鹿皮帽子，真暖和呀……可是虎子没有保护好你们，对不起……虎子我，还不想死！我要当大英雄，我要保护人们，因为……'"
    "刘虎从未如此冷静敏锐，他静静打着秒，算着距离。"
    "熊三十步，鬼子十步……"
    "熊二十三步，鬼子七步……"
    "熊十六步，鬼子四步……"
    "熊扑了过来！就是现在！"
    scene 4_4 with dissolve
    "刘虎迅速侧翻，身体从巨熊的利爪旁擦边闪过。巨熊的爪牙压倒了前来的日本士兵。"
    "刘虎头也不回，竭尽全力往村子跑去，没走一百步，他听到了巨熊的哀嚎，响彻群山。"
    play sound bear_roaring_sound
    play sound gun_sound
    play sound wind_sound

    # 镜头5：自卫队的埋伏
    scene 4_5 with dissolve
    "1931 年的东北冬天，真冷啊。"
    "算起来，东北有四十多个民族，几万个村子，三千万人。"
    "有些事，有为什么吗?谁在创造苦难?谁在歌颂苦难?谁在承受苦难?谁在直面苦难?"
    "我们活着，我们努力着，我们反抗着，我们曾经活过。"
    "我们，想在冬至吃一碗热饺子。"
    "雪还在下，仰头向上看去，无数雪片缭乱了世界，荒芜了许多灯光照不到的角落，许多文章不会记述的角落。"
    "黄昏已至，暮色四合。"
    lisan "各就各位，瞄准了打！"
    zhaohanlie "大家准备好，等我命令再开枪！"
    "心脏，跳，落……跳，落……，如此清晰。"
    "在茅草堆下，在破木屋顶，在道路拐角，在积雪覆盖的每个角落，都有蓄势待发的自卫队士兵。他们都吃过最后一碗饭了，很多人眼睛都哭肿了，视死如归。"
    play sound wind_sound
    play sound villagers_readying_sound

    # 镜头6：战斗爆发
    "鬼子如黑云出现在了北路口，大步走来。寒冷，饥饿，竟然没有打乱他们的步伐，如暴戾的落雪，染黑国土。"
    "鬼子的脚步敲在自卫队的心上。还没到准备攻击的地方。等，等，等……"
    scene 4_6 with dissolve
    "一发子弹提前脱膛而出！"
    zhaohanlie "（来不及纠正）打！"
    lisan "兔崽子们！打准点！"
    "霎时间枪弹如雷电撕裂长夜，火焰化作风暴吞噬战场，电光火石，风林火山！"
    "李三尽情吞吐着胸中点燃的战意，猎枪铿锵上膛，装弹，扣动扳机，贯穿，爆裂，燃烧，撕扯，狂啸，吞噬！"
    play sound gun_sound
    play sound battle_roar_sound

    # 镜头7：激烈的战斗
    "敌人开始寻找掩体，但不知，在经过道路拐角，经过房屋附近，经过坑洼的土地，都有自卫队将士手持刀斧等待。"
    scene 4_7 with dissolve
    "敌军共十四人，须臾之间已死亡六人，伤三人。但硝烟之中，燃尽的漆黑大地上，敌军迅速找到了位置进行反击！"
    "一颗手雷炸塌一座木屋，其上的自卫队士兵纷纷倒地。有位队员的胸口中弹，从屋顶摔倒在地。一位队员被刺刀刺中心脏，挥舞的柴刀停在了半空。一位队员被手雷炸中，爆裂的碎片顷刻间将他吞噬。"
    "将士们目眦欲裂，气冲斗牛。胜利属于每一个人，胜利属于平凡人。"
    "在混乱的战局中，敌方少佐龟田，被不知是谁发射的子弹击杀，随着他狂热的左翼思想灰飞烟灭。"
    zhangyouxi "大家小心，敌人火力很猛！"
    wangxiufeng "我们不能退缩，一定要保护村子！"
    play sound explosion_sound
    play sound battle_roar_sound

    # 镜头8：赵汉烈的牺牲
    "敌军边打边退，意图撤离，自卫队迅速进行拦截。赵汉烈身先士卒，带队进行追击。"
    "往前奔跑，开枪，冲锋，无惧敌方枪林弹雨，穿过死亡之墙！"
    "地上一个人抓住了赵汉烈的腿，把他拽倒在地！该死！赵汉烈挥枪托砸去，这个日本兵用枪回击。"
    scene 4_9 with dissolve
    "没有任何防御，刺刀，贯穿了赵汉烈的胸膛。"
    zhaohanlie "（拼尽全力呐喊）兄弟们，继续战斗，不能让鬼子得逞！"
    "众人本要扶起赵汉烈，听到这话只好含泪继续前进。"
    "敌人在强大火力掩护中逐渐撤离，自卫队成员无论再怎么舍生忘死，也没留住他们。"
    play sound gun_sound
    play sound battle_roar_sound

    # 镜头9：刘虎的愤怒
    scene 2_bg4_1_the village_bg with dissolve
    liuhu "（声嘶力竭）你们这些王八蛋！我要把你们碎尸万段！你胆子你们回来啊！逃走算什么本事！逃走算什么本事！啊啊！"
    "刘虎还在追赶，还在前进，还在拼尽全力追上仇人。"
    "他追到山上，他被石头绊倒，他被子弹打伤胳膊，他的帽子被子弹打飞，他被树枝划伤，他喘不上气，他又一次看着重要的人在眼前死去而无能为力。"
    "他躺在雪地上，看着天空，紧咬嘴唇，愤恨地锤着土地。"
    play sound gun_sound
    play sound battle_roar_sound
    play sound liuhu_panting_sound

    # 镜头10：李三的决断
    scene 4_8 with dissolve
    "敌方死七人，伤四人，还有作战能力的六人。"
    "自卫队死十五人，伤八人，已经失去了信息差优势。算是，开了个好头吗?"
    lisan "今晚，敌人应该不会再来进攻了，他们不熟地形，摸黑的劣势和奇袭的优势抵消。他们多半在山上什么地方扎营。"
    zhangyouxi "（呆呆地看着草草给赵汉烈和其他牺牲将士们立下的木碑）算是，开了个好头吗？"
    lisan "（猛拍张有喜的肩膀）听着！没时间发呆，没时间哀伤已经死了的人了！我要去上山找到鬼子营地，再解决几个，如果回不来，你就是自卫队的总指挥！"
    zhangyouxi "我们会赢吗？"
    lisan "（给张有喜胸口来了一拳）不要对不起大家的牺牲。没什么，要么下半辈子平平安安，要么下辈子平平安安。哈哈，好了，我走了！"
    liuhu "（一瘸一拐地过来）让我也去！"
    "李三毫不理睬刘虎，提枪就往雪山上走去，没入林中……"
    play sound fire_sound
    play sound wind_sound
    play sound lisan_walking_sound

    # 镜头11：李三的偷袭
    scene 2_bg5_9_on_the_mountain_bg with dissolve
    lisan "（自言自语）一枪，正中敌人头部。"
    "李三躲在树上，一枪击中敌人头部。但未等第二枪发射，敌人就投掷了手雷，把他从树上炸了下来。"
    "李三迅速翻滚入最近的枯草堆中，迅速换弹，上膛。敌人用子弹扫射着周围，火焰四起。李三穿过汹涌的火焰，第二颗子弹精准地射入敌人腹部。"
    lisan "（自言自语，轻笑一声）穿过火焰，继续战斗。"
    "李三迅速站起，遁入丛林中向山下跑去，剩下的四个敌人分四路包抄李三。"
    "枪从左耳擦过，右腿被打中，李三举枪回击，却打入白桦树里。李三不断在树木间腾挪变换，身影敏捷如狐。"
    "手雷爆炸，冰雪、黑土、残枝四溅，树枝扎入到李三的右手臂里。李三换用左手举枪，装填，发射！虽然左手并不习惯，但还是成功击中了一个敌人的手臂！"
    "李三可不是匹夫，他有着七成的把握撤退才选择来这里偷袭！借助对山林的熟悉，李三和敌人的距离越拉越远。成功甩开，李三虽然右臂受伤，但还是成功撤回到东村的营地。"
    play sound gun_sound
    play sound explosion_sound
    play sound lisan_panting_sound

    # 镜头12：李三的报告
    scene 2_bg4_1_the village_bg with dissolve
    lisan "做好准备！继续战斗！"
    zhangyouxi "（立马迎过李三来，扶着他走进战壕）李叔，局势如何？"
    lisan "打死一个，打中肚子一个，打掉手臂一个，顶多还有四个人能打了！哈哈！"
    "四个敌人朝李三逃亡方向追来，看到了营地，于是以大树为掩体，向营地进攻。"
    "自卫队成员立刻进入状态，跳到战壕里，进行回击。"
    play sound lisan_reporting_sound
    play sound zhangyouxi_concerned_sound

    # 镜头13：自卫队的坚守
    "战斗持续，敌方火力凶猛，且树林掩体，位置灵活，难以捕捉，进入了持久战。"
    "刘虎突然发现有个敌人沿着村子外围往西边潜去。刘虎挣扎着起身，扛起一把锈迹斑斑的猎枪就翻过墙瓦追去。"
    "轰隆一声巨响，李三所在的战壕被手雷炸中！"
    scene 4_12 with dissolve
    lisan "站起来吧，继续战斗，为了自由！"
    "在一片烽烟里，李三从战壕爬起，拖着千疮百孔的身体，发动最后一次冲锋。"
    "摇晃着，颤颤巍巍地，豁出最后一口气，前进，前进，前进。"
    "大家从战壕里跟随着冲锋，万众一心，共御外敌，前进，前进，前进。"
    "不过是喝了一辈子稀饭的人，哪来的这么大勇气呢?"
    "不过是一些总想着吃香喝辣的人，哪来的这么多无私呢?"
    "不过是一些屈服于生活的人，哪来的这么大力量呢?"
    "保家卫国的心情，这样神奇。"
    play sound battle_roar_sound
    play sound explosion_sound

    # 镜头14：刘虎的追击
    "最后的敌人，向村西边潜行而去，执行最疯狂的报复。"
    liuhu "王八蛋！你给我拿命来！我的爹！我的娘！全是被你们给害死的！"
    play sound gun_sound
    play sound liuhu_panting_sound

    # 镜头15：张有喜的保护
    scene 4_13 with dissolve
    "张有喜也在跟着追击敌人，奈何这个敌人身手实在太过敏捷，根本无法追到！村北村东全部撤离，现在村里老弱妇孺都聚集在村西！开枪，打在墙角。再一次抡足力气上膛，开枪，又擦敌人身侧而过。已经能看到村西头的人们了！"
    zhangyouxi "大家快逃！"
    "最后的敌人开枪射中了一名老人，老人在严冬结束前倒下。大家惊慌四散，敌人突然回过枪来，子弹打中了张有喜的左肩。不行，绝对不能停下来！"
    play sound gun_sound
    play sound zhangyouxi_pain_sound

    # 镜头16：刘虎的牺牲
    "最后的敌人一个侧翻，翻过了一堵矮墙，进入了一个院子。"
    "尖叫声和枪声同时传来！"
    "刘虎和张有喜翻进院子，却发现敌人从院子的另一头逃去，只留下一个抱着孩子痛哭不已的母亲。"
    liuhu "我为什么……救不了他们?"
    "敌人在街巷之间不断逃窜，刘虎和张有喜无论怎样开枪，都没能击中敌人。"
    liuhu "（声嘶力竭）无耻小人！无耻！给我停下！"
    "子弹！刘虎和张有喜发现子弹已经全部用光！"
    "幸运的是，精疲力尽的敌人，最终还是被二人逼到了一个院子里。然而敌人立马转守为攻，向二人开枪，形势被瞬间逆转。"
    "第一发子弹扫中张有喜的左臂。忍耐住极大的疼痛，张有喜和刘虎借装弹空隙举枪向敌人砸来！"
    "然而第二颗子弹在二人攻击到之前就已经装填完成！"
    "嘭！一声枪响，刘虎的胸膛，被贯穿。"
    liuhu "（高举着手臂，痛苦地倒地）还……我……爹……娘！"
    "用尽最后的气力，他高举着枪托，重重砸到敌人的头颅。"
    "敌人受重击倒地，张有喜立刻接续刘虎的战斗，继续向敌人劈砸！"
    "谁知受重伤的敌人却飞速掏出腰间的手枪，正中张有喜腹部。"
    play sound gun_sound
    play sound liuhu_dying_sound

    # 镜头17：张有喜的倒下
    scene 4_15 with dissolve
    "一枪，两枪，三枪，连射三枪，张有喜腹部被强大的冲击力震得连连后退……"
    zhangyouxi "（遗憾不甘）要……结束了吗？我有没有，的确保护了什么呢？"
    play sound gun_sound
    play sound zhangyouxi_pain_sound

    # 镜头18：现代的醒来
    scene 4_16 with dissolve
    "张有喜在一张温暖的床上醒来，窗外，大厦林立，万家灯火璀璨，流星划过天空，梦幻浪漫。手机上显示时间：凌晨 5:00。"
    zhangyouxi "（自言自语）这是哪里？"
    play sound bed_creaking_sound
    play sound wind_sound

    # 镜头19：现代的生活
    scene familiar people_1 with dissolve
    "张有喜起身，坐电梯下楼，去看看外面。他看见早餐摊上便宜的热油条，热粥。他看见随心所欲向父母撒娇的孩子。他看见川流不息，五光十色，与花香鸟语。"
    zhangyouxi "（自言自语）这就是和平的生活吗？"
    play sound elevator_sound
    play sound street_noise

    # 镜头20：熟悉的人们
    scene _2 with dissolve
    "后来，他看见李大娘和儿子在村子里种田务农，安定平安。"
    scene _3 with dissolve
    "他看见王秀凤在大学读书，发挥着自己的天赋，把握未来的方向。"
    scene _4 with dissolve
    "他看见赵汉烈戍守一方，将青春奉献给自由平等的新中国。"
    scene _5 with dissolve
    "他看见小双和爸爸妈妈一起去游乐园，"
    scene _6 with dissolve
    "村长在家准备大展厨艺。"
    scene _7 with dissolve
    "他看见刘虎逃学回家，挨爸妈一顿熊后吃着爸妈做的，他最喜欢的烤肉。"
    zhangyouxi "（自言自语）他们都过得很好。"

    # 镜头21：最后的告别
    scene 4_13 with dissolve
    "就这样，度过了一天。最后，在第二天的凌晨，趁家人熟睡，他轻轻走进家人的房间，帮家人盖好被子。"
    "然后醒来。"
    "他伸出的手得到回握。睁开虚弱的双眼，他看到王秀凤用柔弱的身躯护住了他，千疮百孔。掌心的温暖，从她传递而来。"
    play sound family_breathing_sound
    play sound gentle_touch_sound

    # 镜头22：最后的战斗
    scene 4_14 with dissolve
    "他接过来王秀凤舍命送来的枪，将生命压进枪膛，击穿敌人的胸口。"
    scene Japanese devils go die_1 with dissolve
    scene Japanese devils go die_2 with dissolve
    "弥留之际，他和她紧紧相拥，他最后一次睁眼，看见敌人挣扎着想要爬走。"
    "但老人，孩子，抄起耙子，棍子，砖头，向敌人砸去。"
    "下雪了呢，寒冷却温暖的冬天啊。"
    play sound gun_sound
    play sound battle_roar_sound
    play sound snowfall_sound

    return
