let BreathBubble = document.querySelector(".breath_bubble")
let start = document.querySelector(".start")
let reset = document.querySelector(".reset")

let inhale_1 = document.querySelector("#inhale_1").value * 1000;
document.documentElement.style.setProperty('--inhale_1-time', (inhale_1/1000) + "s");

let exhale_1 = document.querySelector("#exhale_1").value * 1000;
document.documentElement.style.setProperty('--exhale_1-time', (exhale_1/1000) + "s");

let inhale_2 = document.querySelector("#inhale_2").value * 1000;
document.documentElement.style.setProperty('--inhale_2-time', (inhale_2/1000) + "s");

let exhale_2 = document.querySelector("#exhale_2").value * 1000;
document.documentElement.style.setProperty('--exhale_2-time', (exhale_2/1000) + "s");

let inhale_3 = document.querySelector("#inhale_3").value * 1000;
document.documentElement.style.setProperty('--inhale_3-time', (inhale_3/1000) + "s");

let exhale_3 = document.querySelector("#exhale_3").value * 1000;
document.documentElement.style.setProperty('--exhale_3-time', (exhale_3/1000) + "s");

let inhale_4 = document.querySelector("#inhale_4").value * 1000;
document.documentElement.style.setProperty('--inhale_4-time', (inhale_4/1000) + "s");

let exhale_4 = document.querySelector("#exhale_4").value * 1000;
document.documentElement.style.setProperty('--exhale_4-1-time', (exhale_4/1000) + "s");

let post_inhale_ht = document.querySelector("#post_inhale_ht").value * 1000;
document.documentElement.style.setProperty('--post_inhale_ht', (post_inhale_ht/1000) + "s");

let post_exhale_ht = document.querySelector("#post_exhale_ht").value * 1000;
document.documentElement.style.setProperty('--post_exhale_ht', (post_exhale_ht/1000) + "s");

let recovery_inhale = document.querySelector("#recovery_inhale").value * 1000;
document.documentElement.style.setProperty('--recovery_inhale', (recovery_inhale/1000) + "s");

let recovery_exhale = document.querySelector("#recovery_exhale").value * 1000;
document.documentElement.style.setProperty('--recovery_exhale', (recovery_exhale/1000) + "s");

let recovery_bh = document.querySelector("#recovery_bh").value * 1000;
document.documentElement.style.setProperty('--recovery_bh', (recovery_bh/1000) + "s");

let inhale_reps = document.querySelector("#inhale_reps").value;
document.documentElement.style.setProperty('--inhale_reps', (inhale_reps) + "s");

let exhale_reps = document.querySelector("#exhale_reps").value;
document.documentElement.style.setProperty('--exhale_reps', (exhale_reps/1000) + "s");

let breath_reps = document.querySelector("#breath_reps").value;
document.documentElement.style.setProperty('--breath_reps', (breath_reps/1000) + "s");

console.log(breath_reps)

// what do i need to do

// 1. Get all single animations working
// all inhales
function Inhale_1() {
    BreathBubble.style.animation = "inhale_1 var(--inhale_1-time) linear forwards";
    };

function Inhale_2() {
    BreathBubble.style.animation = "inhale_2 var(--inhale_2-time) linear forwards";
    };

function Inhale_3() {
    BreathBubble.style.animation = "inhale_3 var(--inhale_3-time) linear forwards";
    };

function Inhale_4() {
    BreathBubble.style.animation = "inhale_4 var(--inhale_4-time) linear forwards";
    };

// all exhales
function Exhale_1() {
    BreathBubble.style.animation = "exhale_1 var(--exhale_1-time) linear forwards";
    };

function Exhale_2() {        
    BreathBubble.style.animation = "exhale_2 var(--exhale_2-time) linear forwards";
    };

function Exhale_3() {
    BreathBubble.style.animation = "exhale_3 var(--exhale_3-time) linear forwards";
    };

function Exhale_4() {
    BreathBubble.style.animation = "exhale_4 var(--exhale_4-time) linear forwards";
    };
    
// hold times
function Inhale_HT() {
    BreathBubble.style.animation = "inhale_ht var(--post_inhale_ht) linear none";
};

function Exhale_HT() {
    BreathBubble.style.animation = "exhale_ht var(--post_exhale_ht) linear none";
};

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
    
    let breathCounter = document.querySelector(".breath_counter").innerHTML;
    

    for (let i = 0; i < breath_reps; i++) {
        // apply the inhale animation
        await animate(BreathBubble, Inhale_1());
        // apply inhale animation
        await animate(BreathBubble, Inhale_HT());
        // apply another animation
        await animate(BreathBubble, Exhale_1());
        // add a done text after the animation finishes.
        await animate(BreathBubble, Exhale_HT());

        BreathBubble.style.innerText = 'something';
        breathCounter++;
        document.querySelector(".breath_counter").innerHTML = breathCounter;

      }
  }

//   await animate(BreathBubble, Inhale_2());

//   await animate(BreathBubble, Inhale_HT());

//   await animate(BreathBubble, Exhale_2());

//   await animate(BreathBubble, Exhale_HT());

//   await animate(BreathBubble, Inhale_3());

//   await animate(BreathBubble, Inhale_HT());

//   await animate(BreathBubble, Exhale_3());

//   await animate(BreathBubble, Exhale_HT());




start.addEventListener('click', () => {
    chainAnimations();
})


reset.addEventListener('click', () => {
    window.setTimeout(() => {
        window.location.reload(true);
    }, 200); 
});



const input = document.querySelector("input[type='number']")

document.querySelector("input[type='number']").addEventListener('change', (event) => {
    document.documentElement.style.setProperty('--inhale-1-time', input.value + "s");
})
