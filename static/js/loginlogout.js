const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});



// document.getElementById('signup-btn').addEventListener('click', function() {
//   var pass = document.getElementById('password').value;
//   var passCnfrm = document.getElementById('cnfrmpassword').value;
//   var msg=document.getElementById('signup-message');
//   if(pass.length != 0 ){
//     if (pass === passCnfrm) {
//       msg.textContent="Passwords Match";
//       msg.style.backgroundColor="#3ae374";
//     } else {
//       msg.textContent="Password Are Not Match";
//       msg.style.backgroundColor="#FF4D4D";
//     }
//   }else{
//     msg.textContent="Password can't be Empty!";
//     msg.style.backgroundColor="#FF4D4D";
//   }
  
// });

document.addEventListener('DOMContentLoaded', function() {
  const passwordInput = document.getElementById('password');
  const confirmPasswordInput = document.getElementById('cnfrmpassword');
  const submitButton = document.getElementById('signup-btn');
  const msg = document.getElementById('signup-message');

  function validatePasswords() {
      const password = passwordInput.value;
      const confirmPassword = confirmPasswordInput.value;
      if(password.length != 0 ){
              if (password === confirmPassword) {
                msg.textContent="Passwords Match";
                msg.style.color="#3ae374";
                submitButton.disabled = false;
              } else {
                msg.textContent="Password Are Not Match";
                msg.style.color="#FF4D4D";
                submitButton.disabled = true;
              }
      }else{
              msg.textContent="Password can't be Empty!";
              msg.style.color="#FF4D4D";
              submitButton.disabled = true;
            
      }
  }

  passwordInput.addEventListener('input', validatePasswords);
  confirmPasswordInput.addEventListener('input', validatePasswords);
});