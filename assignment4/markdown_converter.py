import markdown
import os
import sys

def convert_markdown_to_html(markdown_file_path, output_file_path=None):

    
    # 마크다운 파일이 있는지 확인
    if not os.path.exists(markdown_file_path):
        raise FileNotFoundError(f"마크다운 파일을 찾을 수 없습니다: {markdown_file_path}")
    
    # 마크다운 파일 읽기
    try:
        with open(markdown_file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        print(f"마크다운 파일을 성공적으로 읽었습니다: {markdown_file_path}")
    except Exception as e:
        raise Exception(f"마크다운 파일 읽기 실패: {e}")
    
    # 마크다운을 HTML로 변환 (테이블, 코드 하이라이팅, 기타 확장 기능 포함)
    html_body = markdown.markdown(
        markdown_content, 
        extensions=[
            'tables',           # 테이블 지원
            'codehilite',       # 코드 하이라이팅
            'fenced_code',      # 코드 블록 지원
            'toc',              # 목차 생성
            'nl2br'             # 줄바꿈 자동 변환
        ]
    )

        # HTML 헤더
    html_header = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>마크다운 변환 결과</title>

</head>
<body>
"""
    
    # HTML 푸터 부분
    html_footer = """
</body>
</html>"""
    
    # 완전한 HTML 문서 생성
    complete_html = html_header + html_body + html_footer
    
    # 출력 파일 경로가 지정되지 않았으면 자동 생성
    if output_file_path is None:
        base_name = os.path.splitext(os.path.basename(markdown_file_path))[0]
        output_file_path = f"{base_name}.html"
    
    # HTML 파일로 저장
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(complete_html)
        print(f"HTML 파일이 성공적으로 생성되었습니다: {output_file_path}")
    except Exception as e:
        raise Exception(f"HTML 파일 저장 실패: {e}")
    
    return complete_html
    
def main():

    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    
    try:
        convert_markdown_to_html(markdown_file, output_file)
        print("변환이 완료되었습니다!")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()

