from django.contrib.auth.forms import  UserChangeForm, UserCreationForm  # 사용자 생성 및 변경 폼을 위한 Django 폼 임포트
from django.contrib.auth import get_user_model  # 현재 활성화된 사용자 모델을 가져오기 위한 함수 임포트
from django.urls import reverse  # URL 패턴을 문자열로 가져오기 위한 함수 임포트

class CustomUserCreationForm(UserCreationForm):  # 사용자 생성을 위한 커스텀 폼 클래스 정의
    class Meta:
        model = get_user_model()  # 현재 활성화된 사용자 모델을 설정
        fields = UserCreationForm.Meta.fields + ()  # 기존 필드에 추가 필드를 더함
        
        
class CustomUserChangeForm(UserChangeForm):  # 사용자 변경을 위한 커스텀 폼 클래스 정의
    class Meta:
        model = get_user_model()  # 현재 활성화된 사용자 모델을 설정
        fields = (
            "username", # 유저네임 추가
            "email",  # 이메일 필드 추가
        )
        
    def __init__(self, *args, **kwargs):  # 초기화 함수 오버라이드
        super().__init__(*args, **kwargs)  # 부모 클래스의 초기화 함수 호출
        if self.fields.get("password"):  # 비밀번호 필드가 있는 경우
            password_help_text = (
                "비밀번호는 오른쪽에서 변경이 가능합니다. "'<a href="{}">여기</a>'  # 비밀번호 변경을 위한 도움말 텍스트 설정
            ).format(f"{reverse('accounts:change_password')}")  # 비밀번호 변경 URL을 포함
            self.fields["password"].help_text = password_help_text  # 비밀번호 필드에 도움말 텍스트 설정
