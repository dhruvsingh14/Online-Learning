Sub forLoop_1()

    ' Create a variable to hold the counter
    Dim i As Integer

    ' Loop through from numbers 1 through 10
    For i = 1 To 10

        ' Iterate through the rows placing a value of 1 throughout
        Cells(i, 1).Value = 1

        ' Loop through from numbers 1 through 10
        For j = 1 To 10

        ' Iterate through the columns placing a value of 1 throughout
            Cells(j, i).Value = 1

        ' Call the next iteration
        Next j

    ' Call the next iteration
    Next i

End Sub

Sub forLoop_2()

    ' Create a variable to hold the counter
    Dim i As Integer

    ' Create a variable to hold the number of loops
    Dim loop_number As Integer
    loop_number = 20

    ' Loop through from numbers 1 through the loop_number
    For i = 1 To loop_number

        ' Iterate through the rows placing a value of 1 throughout
        Cells(i, 1).Value = 1

        ' Loop through from numbers 1 through the loop_number
        For j = 1 To loop_number

            ' Iterate through the columns placing a value of 1 throughout
            Cells(j, i).Value = 1

        ' Call the next iteration
        Next j

    ' Call the next iteration
    Next i

End Sub

Sub forLoop_3()

    ' Create a variable to hold the counter
    Dim i As Integer

    ' Create a variable to hold the number of loops
    Dim loop_number As Integer
    loop_number = 20

    ' Loop through from numbers 1 through the loop_number
    For i = 1 To loop_number

        ' Iterate through the rows placing the sum of the row number and column number into each cell
        Cells(i, 1).Value = i + j

        ' Loop through from numbers 1 through the loop_number
        For j = 1 To loop_number

            ' Iterate through the rows placing the sum of the row number and column number into each cell
            Cells(i, j).Value = i + j

        ' Call the next iteration
        Next j

    ' Call the next iteration
    Next i

End Sub

Sub forLoop_4()

    ' Create a variable to hold the counter
    Dim i As Integer

    ' Create a variable to hold the number of loops
    Dim loop_number As Integer
    loop_number = 20

    ' Loop through from numbers 1 through the loop_number
    For i = 1 To loop_number

        ' Iterate through the rows placing the sum of the row number and column number into each cell
        Cells(i, 1).Clear

        ' Loop through from numbers 1 through the loop_number
        For j = 1 To loop_number

            ' Iterate through the rows placing the sum of the row number and column number into each cell
            Cells(i, j).Clear

        ' Call the next iteration
        Next j

    ' Call the next iteration
    Next i

End Sub
