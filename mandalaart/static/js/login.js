//로그인 실패하면 에러메세지 나오도록
function displayErrorMessage() {
  var errorMessage = document.getElementById("error-message");
  errorMessage.style.display = "block";
  errorMessage.textContent = "이메일 혹은 패스워드가 올바르지 않습니다.";
}

//회원가입 페이지로 이동
function gotoJoin() {
  window.location.href = "./join.html";
}

//로그인
function login() {
  const userID = document.getElementById("id_email").value;
  sessionStorage.setItem("userID", userID);

  window.location.href = "";
}
