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

