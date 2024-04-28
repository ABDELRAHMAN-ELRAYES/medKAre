const addBox = document.querySelector(".add-box"),
popupBox = document.querySelector(".popup-box"),
popupTitle = popupBox.querySelector("header p"),
closeIcon = popupBox.querySelector("header i"),
titleTag = popupBox.querySelector("input"),
descTag = popupBox.querySelector("textarea"),
addBtn = popupBox.querySelector("button"),
confirmedTakenBtn=popupBox.querySelector(".confirmed-btn button");

const months = ["January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"];
const Medicine = JSON.parse(localStorage.getItem("Medicine") || "[]");
let isUpdate = false, updateId;

addBox.addEventListener("click", () => {
    popupTitle.innerText = "Add a new Medicine";
    addBtn.innerText = "Add Medicine";
    popupBox.classList.add("show");
    document.querySelector("body").style.overflow = "hidden";
    if(window.innerWidth > 660) titleTag.focus();
});

closeIcon.addEventListener("click", () => {
    isUpdate = false;
    titleTag.value = descTag.value = "";
    popupBox.classList.remove("show");
    document.querySelector("body").style.overflow = "auto";
});

function showMedicine() {
    if(!Medicine) return;
    document.querySelectorAll(".medicine").forEach(li => li.remove());
    Medicine.forEach((medicine, id) => {
        let filterDesc = medicine.description.replaceAll("\n", '<br/>');
        let liTag = `<li class="medicine">
                        <div class="details">
                            <p>${medicine.title}</p>
                            <span>${filterDesc}</span>
                        </div>
                        <div class="bottom-content">
                            <span>${medicine.date}</span>
                            <div class="settings">
                                <i onclick="showMenu(this)" class="fa-solid fa-ellipsis"></i>
                                <ul class="menu">
                                    <li onclick="updateMedicine(${id}, '${medicine.title}', '${filterDesc}')"><i class="fa-solid fa-pen-to-square"></i>Edit</li>
                                    <li onclick="deleteMedicine(${id})"><i class="fa-solid fa-trash"></i>Delete</li>
                                    <li onclick="unconfirmedMedicine(${id})"><i class="fa-solid fa-xmark"></i>unTaken</li>
                                </ul>
                            </div>
                        </div>
                        <div class="confirmed-btn">
                            <button onclick="confirmedMedicine(this)">Taken</button>
                        </div>
                    </li>`;
        addBox.insertAdjacentHTML("afterend", liTag);
        
    });
}
showMedicine();

function confirmedMedicine (button) {
    const newMedicine=button.parentNode.parentNode;
    newMedicine.style.color="#1a4965";
    newMedicine.style.backgroundColor="#638889";
    newMedicine.querySelector(".details").querySelector("span").style.color="white";
    newMedicine.querySelector(".bottom-content").querySelector("span").style.color="white";
    newMedicine.querySelector(".settings").querySelector("i").style.color="white";
    button.style.backgroundColor="white";
    button.style.color="#265073";
    button.classList.add('taken');

    // saveDivsToLocalStorage(div);

};

function unconfirmedMedicine(medicineId) {
    
}


// const divs = JSON.parse(localStorage.getItem('divs')) || [];
// function saveDivsToLocalStorage(div) {
//     divs.push(getDivData(div));
//     localStorage.setItem('divs', JSON.stringify(divs));
// }
// function getDivData(div) {
//     return {
//         className: div.className,
//         style: div.style.backgroundColor
//     };
// }


function showMenu(elem) {
    elem.parentElement.classList.add("show");
    document.addEventListener("click", e => {
        if(e.target.tagName != "I" || e.target != elem) {
            elem.parentElement.classList.remove("show");
        }
    });
}

function deleteMedicine(medicineId) {
    let confirmDel = confirm("Are you sure you want to delete this Medicine?");
    if(!confirmDel) return;
    Medicine.splice(medicineId, 1);
    localStorage.setItem("Medicine", JSON.stringify(Medicine));
    showMedicine();
}

function updateMedicine(medicineId, title, filterDesc) {
    let description = filterDesc.replaceAll('<br/>', '\r\n');
    updateId = medicineId;
    isUpdate = true;
    addBox.click();
    titleTag.value = title;
    descTag.value = description;
    popupTitle.innerText = "Update a Medicine";
    addBtn.innerText = "Update Medicine";
}

addBtn.addEventListener("click", e => {
    e.preventDefault();
    let title = titleTag.value.trim(),
    description = descTag.value.trim();

    if(title || description) {
        let currentDate = new Date(),
        month = months[currentDate.getMonth()],
        day = currentDate.getDate(),
        year = currentDate.getFullYear();

        let noteInfo = {title, description, date : `${month} ${day}, ${year}`}
        if(!isUpdate) {
            Medicine.push(noteInfo);
        } else {
            isUpdate = false;
            Medicine[updateId] = noteInfo;
        }
        localStorage.setItem("Medicine", JSON.stringify(Medicine));
        showMedicine();
        closeIcon.click();
    }
});