let BreathBubble = document.querySelector(".breath_bubble")
let start = document.querySelector(".start")
let reset = document.querySelector(".reset")

let inhale_1 = document.querySelector("#inhale_1").value * 1000;
document.documentElement.style.setProperty('--inhale-1-time', (inhale_1/1000) + "s");

let exhale_1 = document.querySelector("#exhale_1").value * 1000;
document.documentElement.style.setProperty('--exhale-1-time', (exhale_1/1000) + "s");

let inhale_2 = document.querySelector("#inhale_2").value * 1000;
document.documentElement.style.setProperty('--inhale_2-time', (inhale_2/1000) + "s");

let exhale_2 = document.querySelector("#exhale_2").value * 1000;
document.documentElement.style.setProperty('--exhale_2-time', (exhale_2/1000) + "s");

let inhale_3 = document.querySelector("#inhale_3").value * 1000;
document.documentElement.style.setProperty('--inhale_3-time', (inhale_3/1000) + "s");

let exhale_3 = document.querySelector("#exhale_3").value * 1000;
document.documentElement.style.setProperty('--exhale_3-time', (exhale_3/1000) + "s");

let inhale_4 = document.querySelector("#inhale_4").value * 1000;
document.documentElement.style.setProperty('--exhale-1-time', (exhale_1/1000) + "s");

let exhale_4 = document.querySelector("#exhale_4").value * 1000;
document.documentElement.style.setProperty('--exhale-1-time', (exhale_1/1000) + "s");

let post_inhale_ht = document.querySelector("#post_inhale_ht").value * 1000;
document.documentElement.style.setProperty('--inhale-hold-time', (post_inhale_ht/1000) + "s");

let post_exhale_ht = document.querySelector("#post_exhale_ht").value * 1000;

let recovery_inhale = document.querySelector("#recovery_inhale").value * 1000;

let recovery_exhale = document.querySelector("#recovery_exhale").value * 1000;

let recovery_bh = document.querySelector("#recovery_bh").value * 1000;

let inhale_reps = document.querySelector("#inhale_reps").value;

let exhale_reps = document.querySelector("#exhale_reps").value;

let breath_reps = document.querySelector("#breath_reps").value;

console.log(post_inhale_ht)

// what do i need to do

// 1. Get all single animations working
function Inhale_1() {
    BreathBubble.style.animation = "inhale_1 var(--inhale-1-time) linear forwards";
    };

function Inhale_HT() {
    BreathBubble.style.animation = "inhale_ht var(--inhale-hold-time) linear none"
}

function Exhale_1() {
    BreathBubble.style.animation = "exhale_1 var(--exhale-1-time) linear forwards"
}
//2. Link them together

function animate(elem, animation) {
    return new Promise((resolve, reject) => {
      // Animation end handler
      function handleAnimationEnd() {
        console.log("animation ended...");
        resolve(elem);
      }
      elem.addEventListener("animationend", handleAnimationEnd, { once: true });
      elem.classList.add(animation);
    });
  }

async function chainAnimations() {
    // apply the zoom animation
    await animate(BreathBubble, Inhale_1());
    // apply another animation
    await animate(BreathBubble, Inhale_HT());
    // apply another animation
    await animate(BreathBubble, Exhale_1());
    // add a done text after the animation finishes.
    BreathBubble.style.innerText = 'something';
  }

function Breath1() {
    Inhale_1;
    setInterval(function () {
        Exhale_1;
    }, inhale_1 + post_inhale_ht)
    console.log("Working")
};

start.addEventListener('click', () => {
    chainAnimations();
})


reset.addEventListener('click', () => {
    Exhale_1();
    console.log("I am working reset button")
})


const input = document.querySelector("input[type='number']")

document.querySelector("input[type='number']").addEventListener('change', (event) => {
    document.documentElement.style.setProperty('--inhale-1-time', input.value + "s");
})
