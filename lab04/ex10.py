tuso = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
so_thap_phan = int(input('Nhập một số thập phân: '))
ky_tu = []
def doi_so_thanh_ky_tu(so):
    for ch in str(so):
        ky_tu.append(tuso[int(ch)])
    return ' '.join(ky_tu)
ky_tu = doi_so_thanh_ky_tu(so_thap_phan)
print(f'{so_thap_phan} là {ky_tu}.')