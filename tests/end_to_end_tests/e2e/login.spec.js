describe('Login Test', () => { 
    
    it('Deve fazer login com sucesso', () => { 
      cy.visit('https://seusite.com/login'); 
      cy.get('#username').type('usuario'); 
      cy.get('#password').type('senha'); 
      cy.get('button[type="submit"]').click(); 
      cy.url().should('include', '/dashboard'); 
    }); 
});

// npx cypress open