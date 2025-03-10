import cv2
import numpy as np
import potrace


def png_to_svg(input_path, output_path):
    # 1. 이미지 불러오기 (흑백 변환)
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # 2. 이진화 (흑백 처리)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # 3. potrace를 위한 데이터 변환
    bitmap = potrace.Bitmap((binary < 128).astype(np.uint8))  # 흑백 반전 필요

    # 4. 벡터화
    path = bitmap.trace()

    # 5. SVG 저장
    with open(output_path, "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {} {}">\n'.format(image.shape[1], image.shape[0]))
        for curve in path:
            f.write('<path d="M ')
            f.write(" ".join(f"{segment.x},{segment.y}" for segment in curve))
            f.write('" fill="black" stroke="none"/>\n')
        f.write("</svg>")


# 사용 예제
png_to_svg("input.png", "output.svg")
