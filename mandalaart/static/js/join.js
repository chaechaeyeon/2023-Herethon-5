//회원가입 실패하면 에러메세지 나오도록
function displayErrorMessage() {
  var errorMessage = document.getElementById("error-message");
  errorMessage.style.display = "block";
  errorMessage.textContent = "* 이미 존재하는 이메일 주소입니다.";
}

//로그인 페이지로 이동
function gotoLogin() {
  window.location.href = "./login.html";
}

//회원가입 성공 페이지
function successJoin() {
  window.location.href = "./successJoin.html";
}
