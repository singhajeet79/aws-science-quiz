const questions = [
  "Q1: What is H2O?",
  "Q2: What planet is known as the Red Planet?"
];

function submitQuiz() {
    const answers = ["A", "B"]; // placeholder
    fetch("/submit", {
        method: "POST",
        body: JSON.stringify({ studentId: "demo", answers })
    }).then(r => r.json()).then(console.log);
}
