describe('My First Test', function() {
  it('Does not do much!', function() {
    expect(true).to.equal(true)
  })
})

describe('Visit localhost', function() {
  it('Take a look at 127.0.0.1', function() {
    cy.visit('localhost')
  })
})

describe('Click', function() {
  it('Take a look at 127.0.0.1', function() {
    cy.visit('localhost')

    cy.contains('New random number').click()
  })
})