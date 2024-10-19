        // Função para buscar o endereço usando o ViaCEP
        function buscaCep() {
            let cep = document.getElementById('cep').value;
            let cepErrorDiv = document.getElementById('cep-error-message');

            cepErrorDiv.innerHTML = '';

            if (cep.length !== 8) {
                cepErrorDiv.innerHTML = '<div class="alert alert-warning mt-2">CEP inválido. Por favor, insira um CEP com 8 dígitos.</div>';
                return; 
            }

            // Faz a busca do CEP usando a API ViaCEP
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (!data.erro) {
                        document.getElementById('street').value = data.logradouro;
                        document.getElementById('neighborhood').value = data.bairro;
                        document.getElementById('city').value = data.localidade;
                        document.getElementById('state').value = data.uf;
                    } else {
                        cepErrorDiv.innerHTML = '<div class="alert alert-danger mt-2">CEP não encontrado. Por favor, verifique e tente novamente.</div>';
                    }
                })
                .catch(() => {
                    cepErrorDiv.innerHTML = '<div class="alert alert-danger mt-2">Erro ao buscar o CEP. Tente novamente mais tarde.</div>';
                });
        }
        // formatar numero de celular
        function formatarNumeroTelefone(input) {
        var numero = input.value.replace(/\D/g, '');

        if (numero.length >= 2) {
            numero = '(' + numero.substring(0, 2) + ')' + numero.substring(2);
        }
        if (numero.length > 3) {
            numero = numero.substring(0, 4) + ' ' + numero.substring(4);
        }
        if (numero.length > 10) {
            numero = numero.substring(0, 10) + '-' + numero.substring(10);
        }

        input.value = numero;
    }
    // Função para validar o número de telefone
    function validarTelefone() {
    var telefone = document.getElementById('phone').value;
    var errorDiv = document.getElementById('error-message');

    errorDiv.innerHTML = '';

    if (telefone.length !== 15) {
        errorDiv.innerHTML = '<div class="alert alert-danger mt-3">Telefone Inválido. O telefone deve estar no formato (XX) XXXXX-XXXX.</div>';
        errorDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
        return false; 
    }
    return true;
    }

    // Função para adicionar uma nova experiência profissional
    let experienceCount = 0;
        function addExperience() {
            experienceCount++;
            const experienceDiv = document.createElement('div');
            experienceDiv.setAttribute('id', `experience_${experienceCount}`);
            experienceDiv.innerHTML = `
                <h4>Experiência ${experienceCount}</h4>
                <div class="form-group">
                    <label for="position_${experienceCount}">Cargo:</label>
                    <input type="text" class="form-control" id="position_${experienceCount}" name="position_${experienceCount}" required>
                </div>
                <div class="form-group">
                    <label for="company_${experienceCount}">Empresa:</label>
                    <input type="text" class="form-control" id="company_${experienceCount}" name="company_${experienceCount}" required>
                </div>
                <div class="form-group">
                    <label for="start_date_${experienceCount}">Início do Período:</label>
                    <input type="date" class="form-control" id="start_date_${experienceCount}" name="start_date_${experienceCount}" required>
                </div>
                <div class="form-group">
                    <label for="end_date_${experienceCount}">Fim do Período:</label>
                    <input type="date" class="form-control" id="end_date_${experienceCount}" name="end_date_${experienceCount}">
                </div>
                <div class="form-group">
                    <label for="description_${experienceCount}">Descrição:</label>
                    <textarea class="form-control" id="description_${experienceCount}" name="description_${experienceCount}" rows="3" required></textarea>
                </div>
                <button type="button" class="btn btn-danger" onclick="removeExperience(${experienceCount})">Remover Experiência ${experienceCount}</button>
                <hr>
            `;
            document.getElementById('experience-container').appendChild(experienceDiv);
        }

        // Função para remover uma experiência profissional
        function removeExperience(number) {
            document.getElementById(`experience_${number}`).remove();
            renumberExperience();
        }

        // Função para renumerar as experiências após uma ser removida
        function renumberExperience() {
            experienceCount = 0; // Reinicializa a contagem
            const experienceDivs = document.querySelectorAll('[id^="experience_"]');
            experienceDivs.forEach((experienceDiv, index) => {
                experienceCount++;
                experienceDiv.id = `experience_${experienceCount}`;
                experienceDiv.querySelector('h4').textContent = `Experiência ${experienceCount}`;
                experienceDiv.querySelector('label[for^="position"]').setAttribute('for', `position_${experienceCount}`);
                experienceDiv.querySelector('[id^="position"]').setAttribute('id', `position_${experienceCount}`);
                experienceDiv.querySelector('[name^="position"]').setAttribute('name', `position_${experienceCount}`);

                experienceDiv.querySelector('label[for^="company"]').setAttribute('for', `company_${experienceCount}`);
                experienceDiv.querySelector('[id^="company"]').setAttribute('id', `company_${experienceCount}`);
                experienceDiv.querySelector('[name^="company"]').setAttribute('name', `company_${experienceCount}`);

                experienceDiv.querySelector('label[for^="start_date"]').setAttribute('for', `start_date_${experienceCount}`);
                experienceDiv.querySelector('[id^="start_date"]').setAttribute('id', `start_date_${experienceCount}`);
                experienceDiv.querySelector('[name^="start_date"]').setAttribute('name', `start_date_${experienceCount}`);

                experienceDiv.querySelector('label[for^="end_date"]').setAttribute('for', `end_date_${experienceCount}`);
                experienceDiv.querySelector('[id^="end_date"]').setAttribute('id', `end_date_${experienceCount}`);
                experienceDiv.querySelector('[name^="end_date"]').setAttribute('name', `end_date_${experienceCount}`);

                experienceDiv.querySelector('label[for^="description"]').setAttribute('for', `description_${experienceCount}`);
                experienceDiv.querySelector('[id^="description"]').setAttribute('id', `description_${experienceCount}`);
                experienceDiv.querySelector('[name^="description"]').setAttribute('name', `description_${experienceCount}`);

                let removeButton = experienceDiv.querySelector('button');
                removeButton.textContent = `Remover Experiência ${experienceCount}`;
                removeButton.setAttribute('onclick', `removeExperience(${experienceCount})`);
            });
        }


    // Função para adicionar uma nova formação acadêmica
    let educationCount = 0;
        function addEducation() {
            educationCount++;
            const educationDiv = document.createElement('div');
            educationDiv.setAttribute('id', `education_${educationCount}`);
            educationDiv.innerHTML = `
                <h4>Formação ${educationCount}</h4>
                <div class="form-group">
                    <label for="institution_${educationCount}">Instituição:</label>
                    <input type="text" class="form-control" id="institution_${educationCount}" name="institution_${educationCount}" required>
                </div>
                <div class="form-group">
                    <label for="course_${educationCount}">Curso:</label>
                    <input type="text" class="form-control" id="course_${educationCount}" name="course_${educationCount}" required>
                </div>
                <div class="form-group">
                    <label for="start_date_education_${educationCount}">Início do Período:</label>
                    <input type="date" class="form-control" id="start_date_education_${educationCount}" name="start_date_education_${educationCount}" required>
                </div>
                <div class="form-group">
                    <label for="graduation_date_${educationCount}">Data de Formação:</label>
                    <input type="date" class="form-control" id="graduation_date_${educationCount}" name="graduation_date_${educationCount}">
                </div>
                <button type="button" class="btn btn-danger" onclick="removeEducation(${educationCount})">Remover Formação ${educationCount}</button>
                <hr>
            `;
            document.getElementById('education-container').appendChild(educationDiv);
        }

        // Função para remover uma formação acadêmica
        function removeEducation(number) {
            document.getElementById(`education_${number}`).remove();
            renumberEducation();
        }

        // Função para renumerar as formações após uma ser removida
        function renumberEducation() {
            educationCount = 0; // Reinicializa a contagem
            const educationDivs = document.querySelectorAll('[id^="education_"]');
            educationDivs.forEach((educationDiv, index) => {
                educationCount++;
                educationDiv.id = `education_${educationCount}`;
                educationDiv.querySelector('h4').textContent = `Formação ${educationCount}`;
                educationDiv.querySelector('label[for^="institution"]').setAttribute('for', `institution_${educationCount}`);
                educationDiv.querySelector('[id^="institution"]').setAttribute('id', `institution_${educationCount}`);
                educationDiv.querySelector('[name^="institution"]').setAttribute('name', `institution_${educationCount}`);

                educationDiv.querySelector('label[for^="course"]').setAttribute('for', `course_${educationCount}`);
                educationDiv.querySelector('[id^="course"]').setAttribute('id', `course_${educationCount}`);
                educationDiv.querySelector('[name^="course"]').setAttribute('name', `course_${educationCount}`);

                educationDiv.querySelector('label[for^="start_date_education"]').setAttribute('for', `start_date_education_${educationCount}`);
                educationDiv.querySelector('[id^="start_date_education"]').setAttribute('id', `start_date_education_${educationCount}`);
                educationDiv.querySelector('[name^="start_date_education"]').setAttribute('name', `start_date_education_${educationCount}`);

                educationDiv.querySelector('label[for^="graduation_date"]').setAttribute('for', `graduation_date_${educationCount}`);
                educationDiv.querySelector('[id^="graduation_date"]').setAttribute('id', `graduation_date_${educationCount}`);
                educationDiv.querySelector('[name^="graduation_date"]').setAttribute('name', `graduation_date_${educationCount}`);

                let removeButton = educationDiv.querySelector('button');
                removeButton.textContent = `Remover Formação ${educationCount}`;
                removeButton.setAttribute('onclick', `removeEducation(${educationCount})`);
            });
        }
