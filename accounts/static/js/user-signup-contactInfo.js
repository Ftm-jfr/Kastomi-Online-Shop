document.addEventListener('DOMContentLoaded', function () {
    const provinceSelect = document.querySelector('select[name="province"]');
    const citySelect = document.querySelector('select[name="city"]');

    provinceSelect.addEventListener('change', function () {
        const provinceId = this.value;
        if (!provinceId) {
            citySelect.innerHTML = '<option value="">ابتدا استان را انتخاب کنید</option>';
            return;
        }

        fetch("{% url 'get_cities' %}?province_id=" + provinceId)
            .then(response => response.json())
            .then(data => {
                citySelect.innerHTML = '';
                data.cities.forEach(city => {
                    const option = document.createElement('option');
                    option.value = city.id;
                    option.textContent = city.name;
                    citySelect.appendChild(option);
                });
            });
    });
});
