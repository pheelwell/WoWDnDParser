        Das System muss die erfassten einzelnen Transportmittel eines Unternehmens aufaddieren und das Ergebnis als „Anzahl der Transportmittel“ im Bereich „SEN“ speichern.
        Das System muss wegfallende Transportmittel eines Unternehmens automatisch aus der „Anzahl der Transportmittel“ des Unternehmens im Bereich „SEN“ rausrechnen.
        Das System muss die hinzukommenden Transportmittel eines Unternehmens automatisch in die „Anzahl der Transportmittel“ des Unternehmens im Bereich „SEN“ einberechnen.





        Given I added the Test Company
        And I am in Test Companys freight-carrier Mask
        When I increase the liquid competence by 10
        Then I see that the overall competence increased by 10


        Given I am in the add freight-carrier Form
        And I fill in the Test Company
        Then I turn on <systempartner> as a systempartner
        Then I see the detail view of the freight carrier
        And I see <systempartner> as a systempartner
        Examples:
            | systempartner |
            | Straße        |
            | Schiene       |
            | Wasser        |
            | Luft          |



        Given I am in the add freight-carrier form
        And I fill in the Test Company
        When I turn on <qualifications> as a qualifications
        And I submit the freight-carrier form 
        Then I see the detail view of the freight carrier
        And I see <qualifications> as a qualification
        Examples:
            | qualifications |
            | Lagerhalle |
            | Stellplätze |
            | Werkstatt |
            | Tankstelle |
            | Notstromaggregat|

