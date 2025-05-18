// Selecionar todos os checkbox de uma lista, conforme o caso em configNotifications.html
document.getElementById('select-all').addEventListener('change', function () {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:not(#select-all)');
    checkboxes.forEach(cb => cb.checked = this.checked);
});
