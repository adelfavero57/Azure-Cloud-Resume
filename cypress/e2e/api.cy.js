describe('template spec', () => {
  it('passes', () => {
    cy.request('https://visitorcounteradf.azurewebsites.net/api/vCounter').as('received')

    cy.get('@received').then((response) => {
      expect(response.body).to.have.property('id')
      expect(response.body).to.have.property('counter')
      expect(response.body.counter).to.be.greaterThan(0)
      cy.writeFile('cypress/fixtures/initial.json', response.body)
    })

    cy.request('https://visitorcounteradf.azurewebsites.net/api/vCounter').as('updated')
    cy.get('@updated').then((response)=> {
      cy.fixture('initial').then((value) => {
        expect(value.counter).to.be.lessThan(response.body.counter)
      })
    })
  })
})