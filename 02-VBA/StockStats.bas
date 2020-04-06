Attribute VB_Name = "Module1"
Sub StockStats()

Dim ws As Worksheet

For Each ws In Worksheets

Dim StartingWs As Worksheet
Set StartingWs = ActiveSheet

Dim Ticker As String
Dim LastRow As Long
LastRow = Range("A" & Rows.Count).End(xlUp).Row

Dim Volume As Double
Volume = 0

Dim SummaryTableRow As Integer
SummaryTableRow = 2

Dim Start As Integer
Start = 2

Dim OpenPx As Long
Dim YrChng As Double
Dim PercentChng As Double
Dim j As Integer

ws.Columns("J:J").Style = "Currency"
ws.Columns("K:K").Style = "Percent"
ws.Columns("L:L").Style = "Comma"

ws.Cells(1, 9).Value = "Ticker"
ws.Cells(1, 10).Value = "Year Change"
ws.Cells(1, 11).Value = "Percent Change"
ws.Cells(1, 12).Value = "Annual Vol"

Dim GreaterCondition As FormatCondition
Dim LessCondition As FormatCondition

Set GreaterCondition = ws.Range("K2:K100000").FormatConditions.Add(xlCellValue, xlGreater, "0")
Set LessCondition = ws.Range("K2:K100000").FormatConditions.Add(xlCellValue, xlLess, "0")

With GreaterCondition
    .Font.Color = vbGreen
End With

With LessCondition
    .Font.Color = vbRed
End With

ws.Columns("I:L").AutoFit

j = 0
Change = 0

For i = 2 To LastRow
    If i <> LastRow Then
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
            Ticker = ws.Cells(i, 1).Value
            Volume = Round(Volume + ws.Cells(i, 7), 0)
            YrChng = ws.Cells(i, 6) - ws.Cells(Start, 3)
            If ws.Cells(Start, 3).Value <> 0 Then
                PercentChng = Round((YrChng / ws.Cells(Start, 3)), 1)
                Else
                    PercentChng = Round((YrChng / 0.0001), 4)
                End If
            ws.Range("I" & SummaryTableRow).Value = Ticker
            ws.Range("J" & SummaryTableRow).Value = YrChng
            ws.Range("K" & SummaryTableRow).Value = PercentChng
            ws.Range("L" & SummaryTableRow).Value = Volume
            SummaryTableRow = SummaryTableRow + 1
            StockTotal = 0
        Else
            Volume = Volume + Cells(i, 7).Value
        End If
    End If
Next i
Next ws
End Sub