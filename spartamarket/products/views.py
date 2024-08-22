from django.shortcuts import render

def index(request):
    return render(request, 'products/index.html')



@require_POST  # 이 뷰는 POST 요청만 허용
def delete(request):
    if request.user.is_authenticated:  # 사용자가 인증된 상태일 경우
        request.user.delete()  # 사용자 계정 삭제
        auth_logout(request)  # 로그아웃 처리
    return redirect("index")  # 'index' URL로 돌아가기