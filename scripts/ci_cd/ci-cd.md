# CI/CD

Configurar um pipeline de integração contínua (ex.: GitHub Actions, Jenkins, GitLab CI).
Criar um arquivo YAML ou Jenkinsfile para rodar os testes a cada push no repositório.

Crie um arquivo .github/workflows/ci.yaml no seu repositório com a seguinte configuração:

```bash
name: CI Pipeline 
on: 
  push: 
    branches: 
      - main 
  pull_request: 
    branches: 
      - main 
      
jobs: 
  test: 
    runs-on: ubuntu-latest 
    
    steps: 
    - name: Check out repository 
      uses: actions/checkout@v2 
      
      - name: Set up Node.js 
        uses: actions/setup-node@v2 
        with: 
          node-version: '14' 
          
      - name: Install dependencies 
        run: npm install 
      
      - name: Run tests 
        run: npm run test
```

Isso vai rodar seus testes automaticamente em cada push ou PR feito na branch main.