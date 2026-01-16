document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("repo-search");
  const projectList = document.getElementById("project-list");

  // Dummy data (later connect to data/projects.json)
  const projects = [
    {
      name: "Sample Project",
      description: "This is a sample project for testing search.",
      github_url: "https://github.com/example/sample-project",
      labels: ["good first issue"],
      language: "JavaScript"
    },
    {
      name: "Test Project",
      description: "Another example project.",
      github_url: "https://github.com/example/test-project",
      labels: ["help wanted"],
      language: "Python"
    }
  ];

  // Render projects
  function renderProjects(items) {
    projectList.innerHTML = items
      .map(
        (p) => `
        <div class="project-item">
          <h3>${p.name}</h3>
          <p>${p.description}</p>
          <small>${p.language} | Labels: ${p.labels.join(", ")}</small>
        </div>
      `
      )
      .join("");
  }

  renderProjects(projects);

  // Real-time search
  searchInput.addEventListener("input", (e) => {
    const query = e.target.value.toLowerCase();
    const filtered = projects.filter(
      (p) =>
        p.name.toLowerCase().includes(query) ||
        p.language.toLowerCase().includes(query) ||
        p.labels.some((label) => label.toLowerCase().includes(query))
    );
    renderProjects(filtered);
  });
});
