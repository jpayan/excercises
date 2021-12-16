import typing

def test(expenditure, d):
    notifications = 0
    count = [0] * 201
    for n in expenditure[:d]:
        count[n] += 1
    for i in range(d, len(expenditure)):
        median = find_median(count, d)
        if expenditure[i] >= median * 2:
            notifications += 1
        count[expenditure[i - d]] -= 1
        count[expenditure[i]] += 1
    return notifications


def find_median(arr, limit):
    middle_values = [0, 0]
    middle_indexes = [(limit - 1) // 2]
    if limit % 2 == 0:
        middle_indexes.append(-(-(limit - 1) // 2))
    for i, value in enumerate(middle_indexes):
        k = 0
        j = 0
        while k <= value:
            middle_values[i] = j
            k += arr[j]
            j += 1
    return sum(middle_values) / len(middle_indexes)


# assert test([10, 20, 30, 40, 50], 3) == 1
# assert test([2, 3, 4, 2, 3, 6, 8, 4, 5], 5) == 2

def activityNotifications(expenditure, d):
    # Write your code here
    notifications = 0
    trailing = sorted(expenditure[:d])
    for i in range(d, len(expenditure)):
        median = get_median(trailing)
        if expenditure[i] >= 2 * median:
            notifications += 1
        del trailing[bisect_left(trailing, expenditure[i - d])]
        insort_right(trailing, expenditure[i])
    return notifications


def get_median(arr):
    middle = len(arr) // 2
    return arr[middle] if len(arr) % 2 == 1 else (arr[middle - 1] + arr[middle]) / 2


# assert activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5) == 2
# assert activityNotifications([10, 20, 30, 40, 50], 3) == 1


def counting_sort(arr, limit):
    count = [0] * (limit + 1)
    for n in arr:
        count[n] += 1
    for i in range(1, limit):
        count[i] += count[i - 1]
    for i in range(1, limit):
        idx = limit - i
        count[idx] = count[idx - 1]
    count[0] = 0
    i = 0
    ordered = [0] * len(arr)
    for n in arr:
        ordered[count[n]] = n
        count[n] += 1
    return ordered


# print(counting_sort([2, 3, 4, 2, 3, 6, 8, 4, 5], 10))


def merge_sort(arr):
    print("IN")
    print(f"ARR: {arr}")
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        print("OUT\n")
        return merge_sort(left) + merge_sort(right) + merge(arr, left, right)
    print("OUT\n")
    return 0

def merge(arr, left, right):
    inversions = 0
    li = 0
    ri = 0
    i = 0
    print(f"ARR BEFORE: {arr}")
    while li < len(left) and ri < len(right):
        print(f"LEFT: {left}")
        print(f"RIGHT: {right}")
        print(f"left[li]: {left[li]} <= right[ri]: {right[ri]}?")
        if left[li] <= right[ri]:
            print("YES, NO INVERSION")
            arr[i] = left[li]
            li += 1
        else:
            print("NO, INVERSION")
            inversions += len(left) - li
            arr[i] = right[ri]
            ri += 1
        i += 1
        print(f"ARR AFTER: {arr}\n")
    arr[i:i + len(left) - li] = left[li:len(left)]
    arr[i:i + len(right) - ri] = right[ri:len(right)]
    print(f"FINAL ARR{arr}")
    return inversions


# l = [2, 3, 4, 2, 3, 6, 8, 4, 5]
# print(f"UNSORTED: {l}\n ")
# print(merge_sort(l))
# print(f"SORTED: {l}")

# l = [7, 5, 3, 1]
# print(f"UNSORTED: {l}\n ")
# print(merge_sort(l))
# print(f"SORTED: {l}")


def commonChild(s1, s2):
    # Write your code here
    # if len(s1) == 0 or len(s2) == 0:
    #     return 0
    # if s1[-1] == s2[-1]:
    #     return 1 + commonChild(s1[:-1], s2[:-1])
    # else:
    #     return max(commonChild(s1[:-1], s2), commonChild(s1, s2[:-1]))
    matrix = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                matrix[i][j] == 0
            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = 1 + matrix[i - 1][j - 1]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[-1][-1]   


# assert commonChild(
#     "UBBJXJGKLXGXTFBJYNLHQPULFILXLMPDQFWIYVBRSRFNETTEGXOHLBVOAJMHLZMTMPSJCPWJGHISUUIKDPPAWVQMZECIEIQUPLMFKENHVLKCJVDDSUPDOZXBZSRMWHLIHENULKFEXVCZIOVHRQHZWMDAYLDLGXSTMPDBGAMEBHOMOGGEBFRITAQVALWGINAOWMTRJLJHGEVJOPCVXZQVDBKOUPFJWHMRXULNNKRUUITTVIXYYSZDECBIBBIIWPDOEMFHDJKUSIFZNOTGIVDIJJVHPOGQHXWERMYNYGYOHJYGNOVFNWWERWMTBZOAXNHTCJIBOCUBXERSJORHOAMALOODYOHXIDEINMDWSNKUKFLMFHZLUIFOVDDSGPRJLUOLSFVNCVZUIWRFLKGCKPHGBWMXGNATTRKPOPYYMTHSRYHVXOGFDVRSKDVHHCTJIRAWOLDFDCRXROEVQXMDVOJSGHUPHDSGAJUFWLILUNCGSEPBIGBDNNAGCHBZHFWVUDPAQXLAXIPLSZWDLRQJOMILYKVJNMGBPARKUUTIHOAFIKIRWWUAZASRTOOYHPNHCANPDHGZEWHKAIBGDAAZLAYRWKRWUKBVTRAMLQKSRYVSRXRYVVBOUEGBMGXAZMTQMAJHKGQCRLAJORKHTVLPWFDOZFWHJXMMHNMQIJOBNALQQMPBHMIZCGRGQKOSTJHQXYXUOFKDYKHEISOYNVJSMLYSTEEBWSPFNWIYVBWEFGTUFRZZJGXSMUQGLKQNJPBLKDTXOZQEHXXGKHJZPUUOCWMXUNIBNTJCUFXRQWZGZSLYADLXFYOOPLJRLSYYYHQQUCFEAHNWZOMOUWAUYRFAWHDUPAOJHHPIWYLQRFXGRUCUOAMDNFVTTWTXREEUFCSXADRQKRLRTWYSOGJQSIQZQJHLFWOHTMTYETCJRBRVNYAWIOTXTVEVJMXSGDBESHKJMWQZLWBPSRQAIVURCOZJUXTKCDVJSTEEEXWZCHIFXCROXLHDDVGSFLRPNLRPNXFUUBATGIZJUUVUXMUWAZGKJBRRJAIVIACJTZICMLIKDJRMPVOHEQNAYZMNDMQFMAJNMQOZBXYIXTZDLUJAPISDFMILADTNCJMWSINHWZNGNJNWCRQBSFZAAQVOVQAHJTGFAQTYBEHMSWYGQOJTNJKVVBXZQHOCBOSSBKVRRVFGEXXRZEEOSTOLDFXEATRULHACAQXYAXDEXHFHHGOBXZNIBHEJMRLLNNHICIFTPCRWIPNCXYYRJRERNDVSZAOXIULLFQROQLUAZXDRSYGWOVNCLUBKKRNBEYKALCZDJCJMPFBQXIIMNOHYWEHYGWBRVGNZYVRHVIOSMCATCNDNHKJQVILGTTJIIYPYWECZWDHUGMYBGOAANHFHRUHHFSNXIPYDTEACTOWCUYEXZIOFVOYOYPRQQSBGCBQSFQMTHMCKADQWTMSPHSDYIMOHHWJADQFCRIZANPLWJDCXYXUKOXEMWVKHBISONBQJLODRNPRSSUMBIUKAINIRZEZSHKPTYYVXTGXCRXAULWYFDTRPWWIYDVGFVLNSLIAZHKLWCHVBUFJWINZWKZNVYJYKJYKJIBOBJRQGGVPADSKQHXPSZHXVAVIWQTXZBBDJMTVVFDMZMCWIPEAXLUJJECGMHETBGCJZWIAMKJPXDRYNYZDVYIXHFNOBGOPKUCXTUDFVZFAMWKBTHZDXQNUMFQRNZZNQPYBSWCFJDGOGBAVORCVMWPPRLOKGFCSUMMUBDHABUEYTGOPRLPYESPONOIQNMUQGBFGULJYRLESRQCYNXLOPTBTOZKPRABIYIUWRWIPWONTDPKNGMPHSEWHGNIIAVKUVIXIQZGPNSXCNPPLMIOXKMNUUIAUABOQMMYRJDVDAYAAYOXOWQAVGBMCMIZTVDGKQVXCWRUCCUHSHWXKLZIKJDKIZZBSMBGNYARWXMMKNIPMBKUKSYBVYLTHLIDEHXBHSNYVYJVINFOKPNQCAZIDRYAWTWODCYHUTVHDLBPAQIJJNDDEMVVADJXIJHHHJEVSCHPNJLAUGUPEZAZJEVTJQWCAUUZISUMSYJPRUBAOCAFMTUHXOWBPRAGKFYPLJUPHWHEEOOWKDXYHISNGQYJTADSPAGQMIVZQZLIZQGMMIOKMTKMCOHDZQRYGIKEJCKOBGHWUJZNNSDSSUPUDTPXNBBOKYZRFCORNYJEQXDXGDTIKQMKZNCANALAIPXFIDROXSCHDSPXUMHIHYRCETHUZQJHLCSNGEMBDDFPNONFMKDFXPYANYIYHSKMLYOJRQFOBWIGTEBZVLQDXNUDHZXNMESUJWWQSMZYRXTHXXCEAFUJVFHYYBEOJEVGBPHYMKWVHCCIARIBUISSSAPDIZRBRMSUBWYEKVUMGPJCBBOCDCLMCZBWBVYRQRREQPLHUNHMHTRGLXXXKZJBLJWYKEOJWIQEYBHWJCLQGHHLASDDMWAHFYZHCZJPXJWZQTDGKTOJRAHCTIDIVHRQUHSCMRDICYAAPQYZEQBMXUEPOTILSIJKEEOJXXFFXWDXBVZYTQJSAUAQKELWVTTQGXAHXJWBKBZWZVZADQSCHFQBMSXLCGNNGDMIPFWNKAVZIQLIHBMABUBXSGXXTREJZYBTFBAVIIKTDAIRPYWQZANPYLDJSHRZPMWIPZJPUQUTXJPKMRNOAYOHPFCVLINPOTRDAZWXZCJMDLHGOOLZTNQXMVPNOUZCDFEYATNLCODMOQLDSPYOAPQITRJLQYEBBTOEOHKJKCCETKIADLYLJOMWLGZSKPJQAPFJFOTPTRDCTUCHKTJMTVIFSCRCADLSGNNIUHXXHKOSTZEZMJRYIYCIWCZQPMJPFNBGGIRBTWQYDTVSKDNXDVVIFEJSKELBNQUGYDVKHOUMFGBABLJAYLZKASVYVLCJALPJCUGCULUCLCZIZUYNRPBOQJZHTCKIHEQYMTYLOHJLOEAKZBCGKAQRJSATNRZUSFOSEQXEEZCDBALXHUALTQVBBAWRFBIWKBESOYXPBZINJPUJIKHUJWTJLKHKKQWQTWZNLHSTHYUVINLTDXFNEFRFEGODSFWXGDWZHAVWRNROFTNYEVEBWKMZZURJKOHOHQTANWSMKBNGQOWQHGWWGWAQPNSFNFAKUJNEHRMBYJTWYXKQCWYVGLSEUZGBIFDCEJKVTUGCEKGOFGXDOPADDEZQSHPOWIDPMRCPEEIBBAIUJFVCGAFVSPOJSUPSRYAFBBPALHFKIBQKZEWNUTESHZCHPJHSQUCIEAKQXQWVNJKYHWCSKUEPDRSYGLYQDLFAHYCOCYOXCUKIDVVROCZFOCQCLIHYKOBQPTRAOPZFMOBQNZXHIPZFTDZJALTSKOYTEYAOAOCYEXBGRQYWUOEAVHQUXBPTMVDMIVOWWURCVCXJBSKGNKDMRKQCIYRYHQJTROFIGSITZACPYJDAYODNXWWIDMMNEQWEVLKJAHXERTAPWJHYDTVGSVXADZLUEEMPRSVRJCNAEOIAUJMCYYMKOSZFRXDSOKMXVXGGXSHZHJSPFKMNPBOBQRXFRGFTOGGCVNSWUTUQFVWQLRXMBRLIHOESBLCCINFAHGSAYJVDZOTGVAFDTCLAKQVQHRXPPWZHVOMUNCYWGCLBHXRCYOIZDHFWVRSGQHQQSXDHIGOTKUZAOZXPCROWQIZWBEDUJTYADZOMLAADXDOHDZJLNGXVENVCPWUPBZCWAWTIJKYTRUMITKRNHTFEUVDHVAGLXJCIQJCBTBTZGVHONTTMAMWRWFETPAKQJMDZPZLQPMEJICRKYBFPBHWLIOCXVDXQDEBHVLXOSYKYBSUAFHLOJQFNAUZGVVLMVINWBEJAGFJOTWFIDEIOXPZESJBZBXVCOYWTDDAILFJOKHJPVCALFABUJAHUEDMBPESMINFHTSSLJTQDTYREYQPNJYYDQBLBCUCEOYVGGZDMGGAVBOVPZHWCFMALQTQWMOEWUOJDYCCUFULJBHDDULAWCDXZTMAICBKRVXWXYTNUVNPLVZVIBKJEMKIXCDSVGDLNDXFMUNEOWSUWQCIYNPAEJCHGEUAKBXGCFGLJRFSTZHERMKGIQQYDYXMKUFESCWIQWKRBNYRASHYXUGYMRUZOGKZKNGQDWRXJUWAZBISCSLYBASSZUEHUVZIGHONWDSDVFTKUOECNMKYMWLLPNKYDINPKSLFYIBNERJIZUSELWCICKHZJVDBUIIXHGKRQGOGCSUIYVHWROOAPWMWMGBYWGBDSTFKXFUIWPJOBFEICKIJHHHLNVUDCEMLWEPKCANBMFGODZQRRXRIPKXBGYWAKOWIHFWWXCTZXJVCSHEXDZAXVQYDHMKTFTWVSZHPDPQFCBHYDT",
#     "WZFPTGLCXKNHAKSFEIXYOHTDCCSDAKYASOBHHDTBEZXRKGKOJOLMEGTPSWQNRODAHQOYMOJDVGVSUSMDMLJLVQZYREJGKMKLXGBQEPYXVCTABIBGSWXFWXIIIKDAOXUWZLNYOWRWAUCQTACZPIZREJGTIBCACYDCGSAUULVWRCDLSMIAPCDPHJEOUPOLYPUDSEBYVIUMPLMGTFWCZKDZOHHSGRZDGGPXCUBINGTMOTEOHGLTPOUGCLLJJYFCJJATPZKJSVVKDBJOCJIUNGJJITGMBSYMJLMOCYEGTFECRMBFSBFLXCPSIOJZONIMPPKXETQEEYHUODXZCZJSGMRPFEIRUBUZMHSHRXNXKHMVEMFCSPQQGVEWOMJXSHDRBSPZTFFBAYKXSVULEHDYTDCWATCQCDDEUZINAXFLMWJLOPVWMAMSTMXKKOXSGLAWMGAIWTYWTPBWYEAKSWKSSDQTWVYDFHNTMLAGJBFUSVXUZCMSMDAUBPQOUYLIGVSWGVTASPISVRYGKCJTSKRXCMQOUVNMIIOMQZGZTGLUSRZXFVRLPKDSTTOTHEBQNJNCAICMFQRISSKYKTQWVLLGLLUCHDCKNXSWKGXHEVJGTLQFZJBAPYPUMYLQJPRJZCSRRPSTJQZGVFINHPRKVMHQUPUAAWVAGZIUMNXXGMWQAZXOFHPIHIMJCJMXVUMFSVYGXIIQOSFCRDXYIBHDAZFCJLQTYPVZUEWHCHABWOBSFZMSDHZUDPLRKWIHKJTJLUDZEGHRERGCEGXAWHXHPNEBANUYQVJDVGTFHOUPIVEHVLYZHELIWZPXLKMRLFIHTBBXPSCZZKFDYNHAHFBACRXGGLWLKZDCKPPHPYHLKVJQNXSZVXXBCREROFCITROSOSILHTCXPTNUETFSWJBNHMIIESTBUPFPRCODHDNHSWUEDBUQLYAPSJNHOVYMHXEOCUAHAMTXAFWRTPGMLIOVXDUKCFIVBRVXWTSJYHYTNGQGVPUEQPZAOLVGHDWBHBRHIFVZHAWZQDMNOUXTNJRPTIASYVQIJLBMMCRNYLHMBPIKGVDPPTGKZZNXXTYGNFKYNQKRCDBKHXYXMGJJQERHDUIGMBVNNDCECRCTAQEJRFKWEAZDJJBVSSGFLQYALBPKCPXUMIELWGRWWHLQLTKZFPKXWTMMIYHLOSZOGELNGJEHTIQKJXLKIUOCVWOZEXMWQMSVEAHQQMYHGIBMSQUPEZNDRJGPGGEYVSHEMAYEEDAMLGUUCOKTMKFJVQMKOWXOLEUCYMSTLWROBVFSIFFELMDPXRFRZMVXTSMBONXRSYSLKDLMTCCATCPNLQUTMIODOVTEBFFJVRXLRHJZLWFOJMQAPTTBOQPBQIUWRBHIVHKCELSUUVYKOHVIPHUGBLFZFEECTYORMHBFQMNDNYJANEAHZEGAGNHZOUYEVLAXJXLKYQKSSMITMPYUHTYXRSXTXYLMFYVXDMJFJCAXUFKJLNRDLERJAPAERTYJJFAUFPKYCILLMPDWKZYPWGHYIUCEDRYAAUAQXSPZMYVPGBJYBABGELVTBRFCMCBRQZIWTFOGMRTWZLTMFKPKJEIXTCQUHBIRIRUZBIRBLQDWDEVQBMNFFHJYVIFATHAZBWKVDPDCAVBQOJUUSBHKKNUVNMXSDDXOAWZWUDFLPBJEDAHLYCHTYXHEFQIJABDKILJYPWLHRXUZYFAJGSREEKIXHKTBLZBYFSJSHJVTNWZZIGJHZHSFWZHLEMBHOYFLQOUPJKLZCOUTAVAJWOTTWNFRZJRTZWUTOGNFTWQXJKRFIEZBEQLVCCHVKMOUOFWNPKAIISJHCZVMBQFBOYVWKAMMSZJTYLUXTOVDUNXKADHSTMFBDRGAIULKUOXIFWHJDXLCSFBIMJGELSAGXEALCLIUVCHESOHYLLJPDKYJICTLFTUAYLJUXZQRVHYGBFEDKEJSXLGBRZFEWDZUWTYRYRRVCZJBWEATAGHSHMABGFBQVXODNHJCGMSYKJETETHKZPJHCTMIGUDRMOKCSBKCQQYOTYHGOYJVAIFYCBKZDVXHSHRSFNIMZNBJLLBNKFXSRXPCOXJBYYEWYCAVCQSJYWGBEXWZIXNLGMNEZTVWSMAPWXHKVCXUCIQOBFDNSJKTMLGRGMHMRSYRZEWSUKKVAGTXWDSFHXTHBCBCQLVTQOPGHXKOZCPCQOGFADJTNNHTMCPPWKRCFFPAPPVQFZSUUHPIZCKOYFZNKSJKNLHFOBWPAZYTOJLRYHTNDLXGWDLMYHUOVBQQZARLKZGCJXHSQMFHJWIUYHNBSHHCOPCMXZLLDCFGLKCGXTYTWLOWNGGBEOZECGZCTMVRMKMWYSHAAACPEILLEPOKDJZKGHCUZKWFBPDGRGBXYUCAEMESCABKAETFXHLFGSDFCDEPRIZVJNWPOCNBALVTJXZQHJFRWLVAVPMRFLZVJAFRZJKUKYJTJRSFXCLMINWSSUFWGZNUNZWLVLZJRIXVWYDDNXCVVZHCTPFTPLEOGAWXLLAAEQUWVJLZKYSXNDOTDJUMSDCABLVCKYWYLGBZGLXEWHRFBOJAIGCDWITRGFDUYFCNEXOKFCRJWRFUUKABRXDXIKBFWQVKIXFEEWUVFTNLKJSXNGNMFQDBSFGPYLBMUVKSMORJWGKGQFGASYIZENJITLEEJGNTTLVABVGSBYOQZJQBOOEEVRHVJHYEXIDYJKWUCNSDDSNTTOIBKDAECIXNYKPJNNGDTXJUBDCNYUUMJPSACOYPZXJCTHULSHQLOAJSQNVNOYGSHRFXYSWXIIJMKPTTLCKUVDWTLITJEJPTQQXAFZHMPCKCNKADEGFBSMMCYSQDFEDQLPUAPPAOAIAHVPIRFWIMTBUZVFNCOBQHIOUJADJQJGHTKLADBXUNTPJEVELRPZXEKXPCHTRKVHBNRJNXAXFHQNRPQZJKGBBJENGTAXGBOUCNEKGOAIKLXEAABOWLXRKPAJBSNVFGOOWOWPNYMKCWQNYRRBYVDXTGRELHZHRWXNKCOYXFCGAMXVZWGWEHQZXNLSENXXURQHXGJFVJMGNPUAJZQEWZWXPYROYCVPLRFBCMDRKXZVEFYWGSVLQAFABEPSOOFOLUBQSYXFDRMWNWWYKMGPWHCYNGAEFBDTKPZXZBMOCTSSAUVLIOVYXVUBPKWOYMEDFDSGGJYVSKLQUGCYSIUCGTBYNPMLSMTMEEIZUDHFQVXSLPEQDLWQFJUNPFAKVDRHJSYDJZFLHIRECPPZZFUGVGAJJXPXVECCLHJGTYITISTNHQGCMFWMDJILIIRHJOOUCMFXVWXNSOJTJHDCRDUNDHQWRTRCECBUALWWMWIQDQBCPFAUSRNNWLBLXSYXAQMEVEOEILOHVEZHNUXVATZVXIBXLTVCVTDYFPZGAJGSMVDHHDWJZAGSRCQHGSZAZDQRVARLPYCTAIEKGHDHXPQTTWGQSCVGOLAUQPLTCVNKANFOSTJIYFPRZXHFZSWYCMDADPYGMTZXICKQGQBNMMHETBDBCCUGYILYVHXVDJVZGLXJNCFUDUDWKKCBBWWFYAAJXAUSVUDPHMPTKHORGLRSBXFPDNMQMJSYCMZMXGQWNPXRWZJEAXRXMJVKVMLYWKMHWPPROVLNBTFXMGLSRNPPWZKHMUORZURRSCFNLUOFAJJVOEZWXOZZBMCKGWWCCXPIUNUPSMYSDSKKYJXFMDVAHODUXEHDNAVZALDXZMKEBBTFLRANQHDCUSXBCNTSLVOHOOUIPJFASOCGOGCMTEVOLRCLOSASVQPTDMQQGAXNSHOTPJMETQCJWXLKQATYGZMHRMROBLDWEOAQPVPNPHUJYSXLPFBRCFJKWZLFYAUQIRVRRBIBXMEHMRDFUKXUTYWMKKVAYFTKGGXOMLNDLEVBMECEKOYSISHGRANUDISOXFELKXCSZARTZAVLJXUZISWMSLKDRBDHBEKGYYYZZJKBSQLBRUXPSDMJFCZSLLYGXTBHYCCKAUUKLUASWFYYPYXYQMHEHIXJVQIHBLABNHINYLVUWZGUXVNQWNVPHGZEHVQCCFNTKEPVABVBXHKEIHHYAJTVBCAUGPWJBQIDEIHFKVLTHEBOMPAYSQMMAVCFCXTRUMIMRZLNAJNRWKRLDTGNLDEACNVOJYUZTCXREGPLPKXFEWPOCESGDPYRJYYZSPWTPALTNZMYAVZDBIAVWKWVBWRPLRSWDHOAWAEIFLXVCTWQXAJHTNYBOBXQGWAICLFLMEICSYMDSKSTJQLTQHELYJTUDUQLNCCVHTSXBWSGGGJXQPPZVUYMYOFSQGSFLMQNWERJORSTYZYJVVKTSDBILTGYMBGAECEOWSAZSHLHWDRAHNEGYEKBR") == 1417
import sys

def minimumAbsoluteDifference(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    min_diff = sys.maxsize
    for i in range(len(arr) - 1):
        curr_diff = sorted_arr[i + 1] - sorted_arr[i]
        min_diff = min(curr_diff, min_diff)
    return min_diff

# assert minimumAbsoluteDifference([3, -7, 0]) == 3
# assert minimumAbsoluteDifference([1, -3, 71, 68, 17]) == 3
# assert minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]) == 1


def luckBalance(k, contests):
    # Write your code here
    max_luck = 0
    important_count = 0
    for luck, importance in contests:
        max_luck += luck
        important_count += importance
    important_contests_luck = sorted([contest[0] for contest in contests if contest[1] == 1])
    for i in range(important_count - k):
        max_luck -= important_contests_luck[i] * 2 
    return max_luck

# assert luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]) == 29

def getMinimumCost(k, c):
    if len(c) == k:
        return sum(c)
    prices = sorted(c, reverse=True)
    min_cost = sum(prices[:k])
    for i in range(k, len(prices)):
        min_cost += ((i // k) + 1) * prices[i]
    return min_cost

# assert getMinimumCost(2, [2, 5, 6]) == 15

def maxMin(k, arr):
    # Write your code here
    min_unfairness = sys.maxsize
    sorted_arr = sorted(arr)
    for i in range(k, len(arr) + 1):
        min_unfairness = min(min_unfairness, sorted_arr[i - 1] - sorted_arr[i - k])
    return min_unfairness

# assert maxMin(3, [10, 100, 300, 200, 1000, 20, 30]) == 20
# assert maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]) == 3
# assert maxMin(2, [1, 2, 1, 2, 1]) == 0
# assert maxMin(3, [100, 200, 300, 350, 400, 401, 402]) == 2


# Write a function that when comparing two trees will output the number of nodes that changed. A node changes when:
# 1. It is removed
# 2. It is added
# 3. Its value changes

# Note: whenever a node is removed, all of its children get removed as well

class Node(typing.NamedTuple):
    key: str
    value: int
    children: typing.List["Node"]

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.key == other.key and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


def count_diff_trees(existing: Node, new: Node) -> int:
    diff = 0
    if existing == None and new == None:
        return diff
    if existing == None or new == None or existing.key != new.key:
        diff += count_nodes(existing) + count_nodes(new)
    elif existing.value != new.value:
        diff += 1
    else:
        existing_children = get_children(existing)
        new_children = get_children(new)
        for key, child in existing_children.items():
            diff += count_diff_trees(child, new_children.get(key, None))
        for key, child in new_children.items():
            if key not in existing_children:
                diff += count_diff_trees(None, child)
    return diff

def get_children(node: Node) -> dict[str: Node]:
    if node == None:
        return {}
    return {child.key: child for child in node.children}

def count_nodes(node: Node) -> int:
    count = 0
    if node != None:
        count += 1
        for child in node.children:
            count += count_nodes(child)
    return count


# Example 1

# //              Existing tree                                        
# //                  a(1)                                                
# //                 /     \                                                          
# //              b(2)     c(3)                                               
# //             /     \      \                                                         
# //            d(4)   e(5)   f(6)                                               

# //      New tree 
# //      a(1)
# //          \
# //            c(3)
# //             \
# //              f(66)


# existing_menu = Node(
#     "a",
#     1,
#     [
#         Node(
#             "b",
#             2,
#             [
#                 Node("d", 4, []),
#                 Node("e", 5, []),
#             ],
#         ),
#         Node(
#             "c",
#             3,
#             [
#                 Node("f", 6, []),
#             ],
#         ),
#     ],
# )

# new_menu = Node(
#     "a",
#     1,
#     [
#         Node(
#             "c",
#             3,
#             [
#                 Node("f", 66, []),
#             ],
#         )
#     ],
# )

# expected_count = 4
# actual_count = count_diff_trees(existing_menu, new_menu)
# print(f"example 1: expected_count={expected_count} actual_count={actual_count}")

# # Example 2

# existing_menu = Node(
#     "a",
#     1,
#     [
#         Node(
#             "b",
#             2,
#             [
#                 Node("d", 4, []),
#                 Node("e", 5, []),
#             ],
#         ),
#         Node(
#             "c",
#             3,
#             [
#                 Node("g", 7, []),
#             ],
#         ),
#     ],
# )

# new_menu = Node(
#     "a",
#     1,
#     [
#         Node(
#             "b",
#             2,
#             [
#                 Node("e", 5, []),
#                 Node("d", 4, []),
#                 Node("f", 6, []),
#             ],
#         ),
#         Node(
#             "h",
#             8,
#             [
#                 Node("g", 7, []),
#             ],
#         ),
#     ],
# )

# expected_count = 5
# actual_count = count_diff_trees(existing_menu, new_menu)
# print(f"example 2: expected_count={expected_count} actual_count={actual_count}")

# Example 3

# existing_menu = Node("a", 1, [Node("b", 2, [Node("c", 3, [Node("d", 4, [])])])])

# new_menu = Node("a", 1, [Node("e", 5, [Node("c", 3, [Node("d", 4, [])])])])

# expected_count = 6
# actual_count = count_diff_trees(existing_menu, new_menu)
# print(f"example 3: expected_count={expected_count} actual_count={actual_count}")

# Example 4

# existing_menu = Node("c", 3, [ Node("g", 7, []) ])
# new_menu = Node("h", 8, [ Node("g", 7, []) ])

# expected_count = 4
# actual_count = count_diff_trees(existing_menu, new_menu)
# print(f"example 4: expected_count={expected_count} actual_count={actual_count}")

class LinkedList:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self._head = LinkedList(None)
        self.size = 0

    def push(self, value):
        item = LinkedList(value)
        item.next = self._head.next
        self._head.next = item
        self.size += 1

    def pop(self):
        item = self._head.next
        self._head.next = item.next
        self.size -= 1
        return item.value

    def peek(self):
        return self._head.next.value

graph = {'a': ['b', 'c'], 'b': ['a'], 'c': ['a', 'd'], 'd': ['c']}

# Find all nodes reachable from a given starting node in a given graph

# By depth first
def depth_first_traversal(starting_node: str, graph: dict) -> set:
    reachable = set()
    visited = set()
    stack = Stack()
    stack.push(starting_node)
    while stack.size > 0:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            reachable.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.push(neighbor)
    return reachable

# print(depth_first_traversal('a', graph))

class Queue:
    def __init__(self):
        self._head = LinkedList(None)
        self._tail = LinkedList(None)
        self._head.next = self._tail
        self._tail.previous = self._head
        self._size = 0

    def enqueue(self, value):
        new_item = LinkedList(value)
        new_item.previous = self._head
        new_item.next = self._head.next
        self._head.next.previous = new_item
        self._head.next = new_item
        self._size += 1

    def dequeue(self):
        item = self._tail.previous
        item.previous.next = item.next
        item.next.previous = item.previous
        self._size -= 1
        return item.value

    def peek(self):
        return self._tail.previous.value

    def is_empty(self):
        return self._size == 0

# By breadth first
def breadth_first_traversal(starting_node: str, graph: dict) -> set:
    reachable = set()
    visited = set()
    queue = Queue()
    queue.enqueue(starting_node)
    while not queue.is_empty():
        current = queue.dequeue()
        if current not in visited:
            visited.add(current)
            reachable.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.enqueue(neighbor)
    return reachable

# print(breadth_first_traversal('a', graph))


graph = {'a': ['b', 'c'], 'b': [], 'c': ['d'], 'd': ['c']}

# Is there a path from a given node to another?
# By depth first
def depth_first_search(starting_node: str, target_node: str, graph: dict) -> bool:
    return target_node in depth_first_traversal(starting_node, graph)


# print(depth_first_search('a', 'd', graph))
# print(depth_first_search('d', 'a', graph))


# By breadth first
def breadth_first_search(starting_node: str, target_node: str, grapt: dict) -> bool:
    return target_node in breadth_first_traversal(starting_node, graph)

# print(breadth_first_search('a', 'd', graph))
# print(breadth_first_search('d', 'a', graph))


class Graph:
    def __init__(self, directed=True):
        self.adjacency_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight=1):
        if from_vertex not in self.adjacency_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adjacency_list:
            self.add_vertex(to_vertex)

        self.adjacency_list[from_vertex].append((to_vertex, weight))
        if not self.directed:
            self.adjacency_list[to_vertex].append((from_vertex, weight))

graph = Graph(directed=True)
graph.add_edge("a", "b")
graph.add_edge("a", "c")
graph.add_edge("b", "c")
graph.add_edge("c", "d")
graph.add_edge("d", "d")
graph.add_edge("c", "a")
graph.add_edge("b", "e")

#      a   b   c   d   e
#     ___ ___ ___ ___ ___
# a  | 0   1   1   0   0
# b  | 0   0   1   0   1
# c  | 1   0   0   1   0
# d  | 0   0   0   1   0
# e  | 0   0   0   0   0

from math import inf
# Find the shortest path to all reachable nodes from a given node in a graph
def dijkstra_shortest_path(starting_node: str, graph: Graph) -> dict:
    distances = {node: inf for node in graph.adjacency_list}
    distances[starting_node] = 0
    visited = set()
    paths = {starting_node: (starting_node, 0)}

    queue = Queue()
    queue.enqueue(starting_node)
    while not queue.is_empty():
        current_node = queue.dequeue()
        for neighbor, weight in graph.adjacency_list[current_node]:
            if neighbor not in visited and neighbor != current_node:
                queue.enqueue(neighbor)
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = (current_node, distance)
        visited.add(current_node)
    return paths

def get_shortest_path(starting_node: str, target_node: str, graph: Graph) -> list:
    path_to_target = []
    paths = dijkstra_shortest_path(starting_node, graph)
    if target_node in paths:
        while target_node != starting_node:
            path_to_target.append(target_node)
            target_node = paths[target_node][0]
        path_to_target.insert(len(path_to_target), starting_node)
    path_to_target.reverse()
    return path_to_target


# print(get_shortest_path('a', 'e', graph))

# Considering a list of positive integers where each item represents the maximum steps you can take
# return the minimum amount of steps to get from index 0 to index size - 1

def get_least_amount_of_steps(steps):
    queue = Queue()
    queue.enqueue(steps[0])
    distances = {i: inf for i in steps}

    while not queue.is_empty():
        pass
    

from random import randint
max_steps = 5
max_nodes = 10
steps = [randint(1, max_steps) for i in range(max_nodes)]
# print(steps)
# print(get_least_amount_of_steps(steps))


# How to detect a cycle in a graph
def isCyclicUtil(node, graph, visited, recStack):

    # Mark current node as visited and 
    # adds to recursion stack
    visited[node] = True
    recStack[node] = True

    # Recur for all neighbours
    # if any neighbour is visited and in 
    # recStack then graph is cyclic
    for neighbour in graph[node]:
        if visited[neighbour] == False:
            if isCyclicUtil(neighbour, graph, visited, recStack) == True:
                return True
        elif recStack[neighbour] == True:
            return True

    # The node needs to be poped from 
    # recursion stack before function ends
    recStack[node] = False
    return False

from collections import defaultdict
# Returns true if graph is cyclic else false
def isCyclic(graph: dict):
    visited = defaultdict(bool)
    recStack = defaultdict(bool)
    for node in graph:
        if visited[node] == False:
            if isCyclicUtil(node, graph, visited, recStack) == True:
                return True
    return False

graph = {0: [1, 2], 1: [2], 2: [3], 3: [0]}
print(isCyclic(graph))