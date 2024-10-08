from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse  # URL 패턴을 문자열로 가져오기 위한 함수 임포트


User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'email']


class CustomUserCreationForm(UserCreationForm):  # 사용자 생성을 위한 커스텀 폼 클래스 정의
    class Meta:
        model = User  # 현재 활성화된 사용자 모델을 설정
        fields = UserCreationForm.Meta.fields + ()  # 기존 필드에 추가 필드를 더함


class CustomUserChangeForm(UserChangeForm):  # 사용자 변경을 위한 커스텀 폼 클래스 정의
    class Meta:
        model = User  # 현재 활성화된 사용자 모델을 설정
        fields = (
            "email",  # 이메일 필드 추가

        )

    def __init__(self, *args, **kwargs):  # 초기화 함수 오버라이드
        super().__init__(*args, **kwargs)  # 부모 클래스의 초기화 함수 호출
        if 'password' in self.fields:
            # 비밀번호 필드의 도움말을 완전히 재정의
            self.fields['password'].help_text = (
                '<a href="{}">비밀번호 변경하기</a>'.format(
                    reverse('accounts:change_password'))
            )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("image",)
