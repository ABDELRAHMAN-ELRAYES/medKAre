
//first drop list (Doctors)

const wrapper1 = document.querySelector(".wrapper1"),
selectBtn1 = wrapper1.querySelector(".select-btn1"),
searchInp1 = wrapper1.querySelector(".input1"),
options1 = wrapper1.querySelector(".options1");

let doctors =  [
    "Steven Kerry",
    "Santiago Lopez",
    "Pavel Novak",
    "Youssef Ibrahim",
    "Maria Rodriguez",
    "Elena Petrova",
    "Priya Patel",
    "Sofia Costa"
];




function addDoctor(selectedDoctor) {
    options1.innerHTML = "";
    doctors.forEach(doctor => {
        let isSelected = doctor == selectedDoctor ? "selected" : "";
        let li = `<li onclick="updateName(this)" class="${isSelected}">${doctor}</li>`;
        options1.insertAdjacentHTML("beforeend", li);
    });
}
addDoctor();

function updateName(selectedLi) {
    searchInp1.value = "";
    addDoctor(selectedLi.innerText);
    wrapper1.classList.remove("active");
    selectBtn1.firstElementChild.innerText = selectedLi.innerText;
}

searchInp1.addEventListener("keyup", () => {
    let arr = [];
    let searchWord = searchInp1.value.toLowerCase();
    arr = doctors.filter(data => {
        return data.toLowerCase().startsWith(searchWord);
    }).map(data => {
        let isSelected = data == selectBtn1.firstElementChild.innerText ? "selected" : "";
        return `<li onclick="updateName(this)" class="${isSelected}">${data}</li>`;
    }).join("");
    options1.innerHTML = arr ? arr : `<p style="margin-top: 10px; color:#1a4965;">Oops! Doctor not found</p>`;
});

selectBtn1.addEventListener("click", () => wrapper1.classList.toggle("active"));


//second drop list (Specialties)
const wrapper2 = document.querySelector(".wrapper2"),
selectBtn2 = wrapper2.querySelector(".select-btn2"),
searchInp2 = wrapper2.querySelector(".input2"),
options2 = wrapper2.querySelector(".options2");

let specialties = [
    "Cardiac surgery",
    "Ophthalmology",
    "Neurology",
    "Oncology",
    "Neurosurgery",
    "Pediatrics",
    "Obstetrics and gynecology",
    "Cardiology",
    "Orthopedics",
    "Urology",
    "Gastroenterology"
];

function addSpecialty(selectSpecialty) {
    options2.innerHTML = "";
    specialties.forEach(specialty => {
        let isSelected = specialty == selectSpecialty ? "selected" : "";
        let li = `<li onclick="updateName(this)" class="${isSelected}">${specialty}</li>`;
        options2.insertAdjacentHTML("beforeend", li);
    });
}
addSpecialty();

function updateName2(selectedLi) {
    searchInp2.value = "";
    addSpecialty(selectedLi.innerText);
    wrapper2.classList.remove("active");
    selectBtn2.firstElementChild.innerText = selectedLi.innerText;
}

searchInp2.addEventListener("keyup", () => {
    let arr = [];
    let searchWord2 = searchInp2.value.toLowerCase();
    arr = specialties.filter(data => {
        return data.toLowerCase().startsWith(searchWord2);
    }).map(data => {
        let isSelected = data == selectBtn2.firstElementChild.innerText ? "selected" : "";
        return `<li onclick="updateName2(this)" class="${isSelected}">${data}</li>`;
    }).join("");
    options2.innerHTML = arr ? arr : `<p style="margin-top: 10px; color:#1a4965;">Oops! Specialty not found</p>`;
});

selectBtn2.addEventListener("click", () => wrapper2.classList.toggle("active"));

