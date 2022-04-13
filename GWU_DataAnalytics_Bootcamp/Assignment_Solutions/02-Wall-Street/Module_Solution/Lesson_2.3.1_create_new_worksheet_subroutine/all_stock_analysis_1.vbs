Sub AllStocksAnalysis()

  Worksheets("All Stocks Analysis").Activate

  Range("A1").Value = "All Stocks (2018)"

  'Create a header row
  Cells(3, 1).Value = "Ticker"
  Cells(3, 2).Value = "Total Daily Volume"
  Cells(3, 3).Value = "Return"
End Sub
