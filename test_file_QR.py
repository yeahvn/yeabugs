import qrcode

# QR 코드에 담을 URL
url = "https://github.com/yeahvn/yeabugs"

# QR 코드 객체 생성
qr = qrcode.QRCode(
    version=1,  # QR코드 크기 (1~40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # 한 칸 크기
    border=4,  # 테두리 두께
)

qr.add_data(url)
qr.make(fit=True)

# 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")

# 파일로 저장
img.save("yeabugs_github_qr.png")

print("QR 코드가 'yeabugs_github_qr.png'로 저장되었습니다.")