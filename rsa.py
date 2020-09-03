from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
p=149930380465516707151079321019435489399072155945793735032334088844599773034021170995501688132861944516938448679935403246643441984203770825485165700862168437691254557323938150173733659070945061763789341407547559935070758242521126066900261360899379463301621378242061934281538210192731229473900396425739817670867
q=170559166199281256887953076784727902849936084815549184550874370897326056825177365209113910954088389779180174518262922176726833811470419181874717574929460298509184863124213663255559781224744696195678069242025195218017449489985102637547369070225979448169459840545693721393354651993457943927480894225788038743661
n=365848589691553391654453815696801609393691558975114732077589431735072735814004481321693204054611153742844719038444697593327493027785795731389621927670788503335861977736740530534583572225955976966446771693720421426616666151538067479984725761741317847115913974275314572559550814811157603376899910638368755166255776849626761808720772583206050387900451906315871548607212450421821284358760939660687558588799753487824506759639032283177034815892289194765173975342074810666614953387403646634191147782168926568900983361174986224868620163303631776464544385042160475855173792780028858673004579549168611488908206940265042017827224145445864849990033230038346962998044409425059655414595541354712964867076540952852074402602485254837693009606256646491881886402251519107628767780560029195077356603998621239496833842620813594476086809217145741837067697701029006079475655230057641122885601163764359304119539318186498359110652713132230601632984636292710845264886583673643096710521658506038045125724977714211793704349604343253187208130136333839351343850952892593409667791896415744436543839302830842902421646274217466522255794836216649020356914498443158290307092169834254304137975684324590877396301465368942446331758175055737212871262544202124864201404357
e=65537
d=171667543985758425014232627985840717336387122108163758500542139626729279212540485673813409388397427405892256280730752710530037468765259171638824687119216443453078833931370749271396524300663719786871097595637432285751800013612137436020725492852419342272435212733486026753609513054804440530485467017884797272879406284689903095072725307517165288748564887361729738358011463377509622604034612759898436024272853796444439505507110804160400608180412245257162062494766079887998276493727771202445125297118556385657613871902180087388189988280105656191733965985878495407148701887047735812018200868151321246119065258205755102189932618492331181731032930671506379119003614308043854723142913145153824556828017544028126772950732350030371733003652817854070184981540813302478821473998511699291112000260313162924676245915026226201977284465842505256191235822318812659628683043195357384607192367037650400361829016395922074065034014120534209020328864830006606839179592932609256661738193663329776230050481312159600570791315455079679469956882283489829258240404557309270261381865785081719442470884775430068193960751589033994677379472095235901602941733635505402949964622214247924792042997962235246007680923289071880896909708764598890244005005286926994431628289
cryptotext='ICCHhzayltixzeuA++PPbDwlialEjQuDBx38ecgQwl5lOTnemrcWYbDeQkIIE5oPQOcSmNX8nmcDgyl4O05jYD7VmDcgwQTIgHeOLovcqGVPHEW4hHSmIR3BB/CBjb3/5+HfeifXF1w+/o148o76D9NtTBYaLk8CTjOscT23PBI8w+WPhHBIPaSbJlDuaHA4Ie6ojsE6mM7cp79dz7bCdAf5a2tUGA6AbNCuP1WVnsBI+IIHX8EDELmBnQ5c13JuYnjHL5lmqL3QK88QwQQ4h/3vUODAWBuzn8meWBgfpqxmHTGJ+du2mRoUTpUBzZy2OxrKdD8J11Hc+yJJJkQe5QgqACbM00K0rTv7kIyB2aB/gUGLNP4IOwV09avUpzLS2PPLgeAVP/JSGYlXZTthy4FlqL5pMN4/+swNnEN6Z+lPzLNe0JB0uNN/yPJ3C3lsSuoFLh0InYI46Tycs8vz1nHQWjQdE6hpD/HpyCbjoC2BE4ugCJKUtmp7mbyDxkjkn5ZkHhrJXK/DF4NQgYmfkZxyLOWsI2UC1niq5qGD3SIspW8NcupyGakYVzD1R9PP8xoxpkjX62f7myXLMmacbJgYe7ExeWdYXMZd76Tnqu9IJJwEO43LZz+w2rqH8DIlhr64JenxaDcIixqFzKmkk6WK71VVT3t788ZxaNhG2yo='
private_key=RSA.construct([n,e,d])
cipher_rsa = PKCS1_v1_5.new(private_key)
sentinel = None
data=cipher_rsa.decrypt(base64.b64decode(cryptotext),sentinel).decode('utf-8')
print(data)