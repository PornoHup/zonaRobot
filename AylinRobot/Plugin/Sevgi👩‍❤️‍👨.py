# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import random, os
from random import choice
from helpers.filters import command, other_filters
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters

sevgi = ["**Sen yeter ki çocukluk yap. Gönlümde salıncağın hazır.**", "**Dokunmadan sevmenin mümkün olduğunu senden öğrendim.**", "**Senin gülüşün benim en sevdiğim mevsim.**", "**Hayal ettiğim ne varsa seninle yaşamak istiyorum.**", "**Bazen öyle güzel gülüyorsun ki, bütün dünya kör olsun istiyorum.**", "**Güneş mi doğdu yoksa sen mi uyandın?**", "**Sabahları görmek istediğim ilk şey sensin.**", "**Burası huzur kokmuş buradan geçmişsin belli.**", "**Manzara seyretmek için gidilen bir yerde bile senden güzel bir görsel olamaz.**", "**Su gibi duru güzelliğin karşısında dili tutulur tüm şairlerin.**", "**Sen daha önce hiç yazılamamış bir şiirin en güzel mısrası gibisin. Öyle gizlenmiş, kendine saklanmış, eşsiz.**", "**Kusursuz tavırların var. Korkunç kararlar verdiğimde beni yargılamadığın için sana minnettarım.**","**O kadar günahsız sevdim ki seni, gözlerine bakarken bile utandım..**","**O kadar güzel gülüyordunki, sevmeden geçemedim...**","**Sen bile bilemezsin gülüşün bende nasıl bahar eder..**","**Güneş çıkdığında Yer hangi hissi yaşıyorsa,bende senin yazdığını gördüğümde aynı hissi yaşıyorum..**","**Bizim Sevgimiz Tabiatın 2 ci güneşidir sevgilim..**","**Sırf senin yüzün gülsün diye,bazen saçma-sapan haraketler yapmayı  göze alıyorum..**","**Mutlu olmak umrumda değil, sen yanımda ol, yeter.**","**Bana yüreğinle gel, bahanelerinle değil...**","**Sana bahçeden gül değil, güneşden atom qoparmak istiyorum, amma yüreğim gibi elinde yanar diye korkuyorum.**","**Çokdur sana sözlerim,aklıma geldikce söylerim,gülümm bu fani dünyada ben sensiz naparım?**","**Sanmaki, yerin dolacak, senden başka biri benle olacak. Ne bana senin gibi bir sevgili ne de seni benim gibi seven bulunacak","`Bəyəm bütün şairlər sənə aşiq idi? Oxuduğum, dinlədiyim hər şeirdə sən varsan`","`Çox sevilməyə deyil, həmişə sevilməyə ehtiyacım var`","`Xoşbəxt olmaq vecimə deyil, sən yanımda ol, yetər`","`Yağış başlayanda gəlsəydi, birlikdə islanardıq, - deyəcəyi biri olmalı insanın həyatında`","`Bir insan aşiq olduqda qısqanar, qışqırar, sorğu-sual edər, hesab soruşar, sahiblənər. Amma anlayana...`","`Gördüyünü hər kəs sevər, sən onda görmədiyini tapacaqsan. Əgər gerçək eşq istəyirsənsə, bədənə deyil, ürəyə toxunacaqsan`","`Açıq çay içərdi həmişə, dəmli olduqda stəkanın digər tərəfindən məni görə bilmirmiş. Belə deyirdi...`","`Eşq üçün yaşadıqlarımı bilsəydin əgər, hələ də sevə bilməyimə aşiq olardın`","`Böyük eşqlər ya sonsuzdur, ya da onsuz...`","`Sevgi kəpənək kimidir. Arxasınca qaçdıqca səndən qaçar. Ən yaxşısı qoy, uçsun, bəlkə heç gözləmədiyin bir anda gəlib çiyninə qonar`","`Bil ki, yıxılmaq deyil insanları kədərləndirən. Əlindən tuturmuş kimi davranıb, əslində itələyənlərdir insanı həyatdan küsdürən`","`Ağrılarıma belə, həzz qatır eşqin. Bütün hüceyrələrimə toxunan məlhəm kimisən`","`Biz səninlə tarix boyu gecikmiş eşqik. Vaxtında çatmadıq xəyal qırıqlarımızı daşıyan gəminin yola düşməyinə...`","`Birisini sevmək , onu qüsurları və yanlışları ilə qəbul etmək deməkdir`","`Bir sevgini anlamaq, bir ömür xərcləməkdir...`","`Heç kim sevgilisinə mənim üçün nə etdin? deməməlidir.. ,7 milyard insanin içində səni tapıb, daha nə etsin?`","`Küsmək və incimək üçün bəhanələr axtarmaq yerinə, sevmək və sevilmək üçün çarələr axtarın...`","`Bir qadının alnı dodaqlarından daha dəyərlidir. Dodaqlarından süzülən “səni sevirəm” əvvəlcədən alnına yazılıb`","`Mənə ürəyinlə gəl, bəhanələrinlə deyil...`","`İnsan okeanda ölməz, ancaq bir qaşıq sevdada boğular`","`Bəziləri danışmaz, gözlərinə 5 saniyə baxar, ömrünün 5 ili gedər`","`Sən getsən səsin gedər, qoxun gedər, üzün gedər. Titrəyərəm, gecəm bitər`","Mən sadəcə səni istədim.Bütün dünyalar başqa qadınların olsun.Mənə sən bəssən.🖤","Sən getsən səsin gedər, qoxun gedər, üzün gedər. Titrəyərəm, gecəm bitər","Ayrılığın sevgiyə olan təsiri, küləyin oda olan təsiri ilə eynidir. Kiçik sevgiləri öldürər, böyük sevgiləri dahada alovlandırar","•sᴇᴠɢɪᴅəɴ s‌ᴜ‌ʙʜə ᴇᴛᴍəʏɪɴ, sɪᴢɪ əsʟ sᴀғ sᴇᴠɢɪ ɪʟə sᴇᴠəᴄəᴋ ʙɪʀɪɴɪɴ ɢᴏ‌ᴢᴜ‌ɴᴅə ʜəᴍɪs‌ə ᴍᴜ‌ᴋəᴍᴍəʟ ᴏʟᴀᴄᴀϙsıɴıᴢ","Ay günəşi sevмəк ilə o qədər мəşğul idi кi, ulduzların нəя gecə onun üçün necə işıqlandığını görməmişdi.","Bir insan bir gunde 100 dene insan gorur amma menim gozüm tekce seni gorur ♡","Sonsuz kainatda bütün ulduzlar toplaşsa senin qeder aydinlada bilmez ureyimi♡","Sene olan sevgim küleye oxşuyur.Görünməz və sonsuz♡","1 çiçek sene olan sevgimi gösterseydi eger dünya gül bağçasi olardi♡","Men şeheri izlemeyden bezdim Sxilmadan izleyeceyim tek menzerem sen ol♡","Sinəmdə döyünən, çırpınan ürək deyil. Sənsən!","Bezileri kimi sevdiyimden yana dünyani dagitmaxa gucum çatmaz ama seni her zaman sevmeye çatar (axrinci nefesime kimi)♡","Allah her kese 1 melek verir menimkide sensen ama göze görünen melek sen-sen😂♡","Aynaya baxınca özümü deyil, böyük bir 💓ürək və o ürəkdə ondan da böyük səni gördüm.","  Səni sevməyimə və bunun müqabilində məni sevdiyinə görə təşəkkür edirəm. Mənim olduğum üçün çox şanslıyam. ❤️ Sevgililər günümüz mübarək sevgilim!"," Bütün şairlər sənəmi aşiq idi ki hər oxuduğum şeirdə, dinlədiyim mahnıda sən var idin"," 🌃Gecəyə inad ☀️gün ağarmaqda, 🌳Ağaca inad budaq çoxalmaqda, Ölümə inad 🧍‍♂️insanlar çoxalmaqda, Mən isə sənə inad səni sevməkdəyəm... İnad budur eee həmişə də sevəcəyəm​​🥰","❤️ Sevmək çətin iş, nə 💵 maaşı var nə sığortası, Bir ayrılığı var bir də 😭gözyaşı.","Gecədirmi insanı 😔kədərləndirən, yoxsa insandırmı kədərlənmək üçün gecəni gözləyən? Gecədirmi səni mənə düşündürən yoxsa mənəmmi səni düşünmək üçün gecəni gözləyən?😕","❤️ Sevirsənsə bu gün soruş, bu gün ara, sabaha kim ölə, kim qala..?","🙈Kor, 🙉kar və 🙊dilsiz çöldə gedirlər, kar ölür. Dilsiz, kora karın öldüyünü necə izah edər? ❤️səni sevmək də elədir.","Sevmək öz xoşbəxtliyini başqasının xoşbəxtliyində tapmaqdır.","Sevgili, axtarıb da tapdığın biri deyil, heç ağılında yoxkən aşiq olduğun adamdır.","Dünyanın ən gözəl ritmi, onun sənin üçün döyünən ürəyidir.","Hər bir zərrəm aşiqdir hər bir zərrənə.","Sən mənim göylərə göndərdiyim dualarımın yer üzündəki cavabısan.","Gözəl danışmaq üçün tək bir yol vardır; dinləmək. -Bob Marli","Bu dünyada həqiqəti deməkdən daha çətin və yalan danışmaqdan daha asan heç nə yoxdur. - Dostoyevski","Hər şeyə əsəbiləşən, boş yerə hay-küy salanan ya lovğadır, ya da ağılsız. - Aleksandr Pop","Quyuya salsan da yaxşılığı, bil Yenə qayıdacaq, o itən deyil.","Ürəkdən gələn söz həmişə ürəklərə yol tapar.","İncitək sözlər seç, az danış, az din,Qoy az sözlərinlə dünya bəzənsin.","Söz gözəl olursa-olsun nə qədərPis əda o sözü tamam məhv edər.","İnsana arxadır onun kamalı,Ağıldır hər kəsin dövləti, malı.","Amandır ağlını unutma ki sən Gülü tikana dəyişməyəsən.","Çox gözəl olsa da eybi gizləmək Dost dostun eybini örtməsin gərək.","Yaxşılıq etməsən əgər insana Böyüklük şerefdi","`Nefes almaq üçün pencereni deyilde sekilini açanda anladim bezi seyleri...🖤💫`","`Heç bir şey birlikdə xoşbəxt olmaqdan daha özəl və gözəl deyildir..🤍`","`Dünyanin en gözel ritmi, onun senin üçün döyünen üreyidir..🖤`","`Minlerce ömrüm olsa, hamsinda tekrar-tekrar senle qarşılaşmağı seçerdim.❤️`","`Sevgi qelbini bir başqasinin merhemetine buraxmaq imiş...❣️`","`On tanesiyle yol yürümek değil, bir tanesiyle yolu bitirmek asıl mesele`","`Sən mənim kiçik ürəyimin böyük dünyasısan.❣ ┄┅═══✼🍃🌸🍃✼═══┅┄Ты большой мир моего маленького сердца.❣`","`Senle konuşmayı bıraktıklarında Senin hakkında konuşmaya başlarlar.💙🖤","`🖤Qucaqla məni, qabırğalarım sənin əllərinə həsrətdir`"]



@app.on_message(command("sevgi") & ~filters.edited)
async def alive(bot: Client, msg: Message):
    await msg.reply(random.choice(sevgi))