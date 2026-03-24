const num_people = document.getElementById('num_people');
const highHit = document.getElementById('highHit');
const lowHit = document.getElementById('lowHit');

function updateHitRange() {

    const selectedValue = num_people.value;
    let max = 0;
    if (selectedValue === "4") {
        max = 16;
    } else if (selectedValue === "5") {
        max = 20;
    } else if (selectedValue === "6") {
        max = 24;
    }

    // 両方クリア
    highHit.innerHTML = "";
    lowHit.innerHTML = "";

    for (let i = 0; i <= max; i++) {

        // highHit
        const highOption = document.createElement("option");
        highOption.value = i;
        highOption.textContent = i;

        if (i === max) {
            highOption.selected = true;
        }

        highHit.appendChild(highOption);

        // lowHit
        const lowOption = document.createElement("option");
        lowOption.value = i;
        lowOption.textContent = i;

        if (i === Math.ceil(max/2)) {
            lowOption.selected = true;
        }

        lowHit.appendChild(lowOption);
    }
}

// 変更時
num_people.addEventListener('change', updateHitRange);

lowHit.addEventListener("change", () => {
    if (lowHit.value > highHit.value) {
        highHit.value = lowHit.value;
    }
});

highHit.addEventListener("change", () => {
    if (parseInt(highHit.value) < parseInt(lowHit.value)) {
        lowHit.value = highHit.value;
    }
});
