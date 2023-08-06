import requests
import bs4

import gempaterbaru


def ekstrasi_data():
    """
    Tanggal     : 18 Maret 2023,
    waktu       : 02:38:00 WIB
    Magnitudo   : 5.1
    Kedalaman   : 91 km
    Lokasi      : Pusat gempa berada di darat 6 km barat daya Kota Jayapura
    Dirasakan   : Dirasakan (Skala MMI): II - III Kota Jayapura
    :return:
    """
    try:
        content = requests.get("https://bmkg.go.id")
    except Exception:
        return None

    if content.status_code == 200:
        soup = bs4.BeautifulSoup(content.text, "html.parser")

        result = soup.find("span", {"class":"waktu"})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find("div",{"class":"col-md-6 col-xs-6 gempabumi-detail no-padding"})
        result = result.findChildren ("li")
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt= None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split('- ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i  == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict ()
        hasil["tanggal"] = tanggal
        hasil["waktu"] = waktu
        hasil["magnitudo"] = magnitudo
        hasil["kedalaman"] = kedalaman
        hasil["koordinat"] = {'ls':ls, 'bt':bt}
        hasil["lokasi"] = lokasi
        hasil["dirasakan"] =dirasakan
        return  hasil
    else:
        return  None
def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return
    print("Gempa Terakhir beradasarkan BMKG ")
    print(f"Tanggal,{result['tanggal']}")
    print(f"waktu,{result['waktu']}")
    print(f"magnitudo,{result['magnitudo']}")
    print(f"kedalaman,{result['kedalaman']}")
    print(f"lokasi,{result['lokasi']}")
    print(f"koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"dirasakan,{result['dirasakan']}")

if __name__ == '__main__':
    result = ekstrasi_data()
    tampilkan_data(result)
