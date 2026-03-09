const API_BASE_URL = window.API_BASE_URL || "http://localhost:8000";

const form = document.getElementById("risk-form");
const resultBlock = document.getElementById("result");
const errorBlock = document.getElementById("error");

function validatePayload(payload) {
  if (!payload.age || payload.age < 18 || payload.age > 100) {
    return "Возраст должен быть в диапазоне 18-100.";
  }
  if (!payload.height_cm || payload.height_cm < 100 || payload.height_cm > 230) {
    return "Рост должен быть в диапазоне 100-230 см.";
  }
  if (!payload.weight_kg || payload.weight_kg < 30 || payload.weight_kg > 250) {
    return "Вес должен быть в диапазоне 30-250 кг.";
  }
  return "";
}

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

  const validationError = validatePayload(payload);
  if (validationError) {
    errorBlock.textContent = validationError;
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
      const body = await response.json().catch(() => ({}));
      const detail = body?.detail ? ` (${JSON.stringify(body.detail)})` : "";
      throw new Error(`Ошибка запроса к серверу${detail}`);
    }

    const data = await response.json();

    document.getElementById("score").textContent = String(data.score);
    document.getElementById("risk_level").textContent = data.risk_level;
    document.getElementById("recommendation").textContent = data.recommendation;
    document.getElementById("explanation").textContent = data.explanation;

    resultBlock.classList.remove("hidden");
  } catch (error) {
    errorBlock.textContent =
      "Не удалось получить результат. Проверьте запуск backend (http://localhost:8000).";
    console.error(error);
  }
});
