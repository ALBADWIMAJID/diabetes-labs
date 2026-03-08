const API_BASE_URL = "http://localhost:8000";

const form = document.getElementById("risk-form");
const resultBlock = document.getElementById("result");
const errorBlock = document.getElementById("error");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  errorBlock.textContent = "";
  resultBlock.classList.add("hidden");

  const payload = {
    age: Number(document.getElementById("age").value),
    height_cm: Number(document.getElementById("height_cm").value),
    weight_kg: Number(document.getElementById("weight_kg").value),
    physical_activity: document.getElementById("physical_activity").value,
    family_history_diabetes: document.getElementById("family_history_diabetes").checked,
    high_sugar_intake: document.getElementById("high_sugar_intake").checked,
    high_blood_pressure_history: document.getElementById("high_blood_pressure_history").checked,
  };

  if (!payload.age || !payload.height_cm || !payload.weight_kg) {
    errorBlock.textContent = "Проверьте, что все обязательные поля заполнены корректно.";
    return;
  }

  try {
    const response = await fetch(`${API_BASE_URL}/risk-assessment`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error("Ошибка запроса к серверу");
    }

    const data = await response.json();

    document.getElementById("score").textContent = data.score;
    document.getElementById("risk_level").textContent = data.risk_level;
    document.getElementById("recommendation").textContent = data.recommendation;

    resultBlock.classList.remove("hidden");
  } catch (error) {
    errorBlock.textContent = "Не удалось получить результат. Убедитесь, что backend запущен.";
  }
});
