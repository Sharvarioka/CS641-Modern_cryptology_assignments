def coppersmith_howgrave_univariate(pol, modulus):

    dd = pol.degree()
    # PLAY WITH THOSE:
    beta = 1                             # we should have q >= N^beta
    epsilon = beta / 7                     # <= beta/7
    mm = ceil(beta**2 / (dd * epsilon))    # optimized
    tt = floor(dd * mm * ((1/beta) - 1))   # optimized
    XX = ceil(N**((beta**2/dd) - epsilon)) # we should have |diff| < X
    nn = dd * mm + tt

    if not 0 < beta <= 1:
        raise ValueError("beta should belongs in (0, 1]")

    if not pol.is_monic():
        raise ArithmeticError("Polynomial must be monic.")

    # change ring of pol and x
    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)

    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # display basis matrix
    if debug:
        matrix_overview(BB, modulus^mm)

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()
    print("potential roots:", potential_roots)

    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    return roots


# RSA break using coppersmith
def break_RSA(pad_str, max_pass_len):
    global e, C, N
    ZmodN = Zmod(N)
    pad_str_binary = ''.join(format(ord(i), '08b') for i in pad_str)

    for pass_len in range(0, max_pass_len, 8):          # size of the root

        # Problem to equation (default)
        A.<M> = PolynomialRing(ZmodN) #, implementation='NTL')
        pol = ((int(pad_str_binary, 2)<<pass_len) + M)^e - C
        roots = coppersmith_howgrave_univariate(pol, N)

        if roots:
            binary='{0:b}'.format(roots[0])
            return binary,pass_len

    print('No solution found\n')
    return


e = 5
N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C = 23701787746829110396789094907319830305538180376427283226295906585301889543996533410539381779684366880970896279018807100530176651625086988655210858554133345906272561027798171440923147960165094891980452757852685707020289384698322665347609905744582248157246932007978339129630067022987966706955482598869800151693
pad_str="You see a Gold-Bug in one corner. It is the key to a treasure found by "

#finding the root
binary = break_RSA(pad_str, 256)
print("Root length :", len(binary[0]))
print("Root is :", binary[0])


#Padding of the root
if len(binary[0])<binary[1]:
    for i in range(0, binary[1]-len(binary[0])):
        binary='0'+binary[0]
print("Root after padding is :", binary)


# slicing the root and converting it in decimal and then converting it in string
str_data =' '
for i in range(0, len(binary), 8):
    temp_data = binary[i:i + 8]
    decimal_data = int(temp_data, 2)
    str_data = str_data + chr(decimal_data)

print("Password is:", str_data)









