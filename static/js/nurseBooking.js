const wrapper1 = document.querySelector(".wrapper1"),
selectBtn1 = wrapper1.querySelector(".select-btn1"),
searchInp1 = wrapper1.querySelector(".input1"),
options1 = wrapper1.querySelector(".options1");

let nurses =  [
"Mark Johnson",
"Daniel Kim",
"Lucas Martinez",
"Andrei Popov",
"Anna Schmidt",
"Isabella Nguyen",
"Sofia González",
"Amira Ali"
];

function addNurse(selectedDoctor) {
    options1.innerHTML = "";
    nurses.forEach(nurse => {
        let isSelected = nurse == selectedDoctor ? "selected" : "";
        let li = `<li onclick="updateName(this)" class="${isSelected}">${nurse}</li>`;
        options1.insertAdjacentHTML("beforeend", li);
    });
}
addNurse();

function updateName(selectedLi) {
    searchInp1.value = "";
    addNurse(selectedLi.innerText);
    wrapper1.classList.remove("active");
    selectBtn1.firstElementChild.innerText = selectedLi.innerText;
}

searchInp1.addEventListener("keyup", () => {
    let arr = [];
    let searchWord = searchInp1.value.toLowerCase();
    arr = nurses.filter(data => {
        return data.toLowerCase().startsWith(searchWord);
    }).map(data => {
        let isSelected = data == selectBtn1.firstElementChild.innerText ? "selected" : "";
        return `<li onclick="updateName(this)" class="${isSelected}">${data}</li>`;
    }).join("");
    options1.innerHTML = arr ? arr : `<p style="margin-top: 10px; color:#1a4965;">Oops! Nurse not found</p>`;
});

selectBtn1.addEventListener("click", () => wrapper1.classList.toggle("active"));




document.getElementById('booking-form').addEventListener('submit', function(event) {

    let selectedDoctor = selectBtn1.firstElementChild.innerText.trim();

    let hiddenInput = document.createElement('input');
    hiddenInput.type = 'hidden';
    hiddenInput.name = 'nurse_name';
    hiddenInput.value = selectedDoctor;

    this.appendChild(hiddenInput);
});