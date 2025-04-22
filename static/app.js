async function getRepos() {
    const keyword = document.getElementById("searchBox").value;
    const list = document.getElementById("resultList");
    list.innerHTML = "Загрузка...";

    const res = await fetch(`/api/search?keyword=${encodeURIComponent(keyword)}`);
    const data = await res.json();

    list.innerHTML = "";

    if (data.status === "ok") {
        data.data.forEach((repo, i) => {
            const item = document.createElement("li");
            item.innerHTML = `<strong>${i + 1}. <a href="${repo.web}" target="_blank">${repo.title}</a></strong> — ⭐ ${repo.stars}`;
            list.appendChild(item);
        });
    } else {
        list.innerHTML = `<li>Ошибка: ${data.message}</li>`;
    }
}
