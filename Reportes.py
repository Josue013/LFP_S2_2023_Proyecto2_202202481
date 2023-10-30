import webbrowser
class Reporte:
    def __init__(self) -> None:
        print("")
    def printTableToken(self,report,lis):
        report.write("""<div class="container"><table class="table">
                                <thead class="letra">
                                    <tr>
                                    <th scope="col">Token</th>
                                    <th scope="col">Lexema</th>
                                    <th scope="col">Fila</th>
                                    <th scope="col">Columna</th>
                                    </tr>
                                </thead>
                                <tbody class="letra">
                                """)
        for tok in lis:
            if tok.getTipo() != "Final":
                report.write("<tr><td>"+tok.getTipo()+"</td><td>"+str(tok.getLexema())+"</td><td>"+str(tok.getFila())+"</td><td>"+str(tok.getColumna())+"</td></tr>")
        report.write(""" </center></tbody>
                                </table></div>""")
    def printTableError(self,report,lis):
        report.write("""<div class="container"><table class="table">
                                <thead class="letra">
                                    <tr>
                                    <th scope="col">Error</th>
                                    <th scope="col">Fila</th>
                                    <th scope="col">Columna</th>
                                    </tr>
                                </thead>
                                <tbody class="letra">
                                """)
        for tok in lis:
             report.write("<tr><td>"+str(tok.getLexema())+"</td><td>"+str(tok.getFila())+"</td><td>"+str(tok.getColumna())+"</td></tr>")
        report.write(""" </center></tbody>
                                </table></div>""")
    def reporteTokens(self,titulo,tokens,sintactico):
        report = open("Reporte"+titulo+".html","w")
        report.write("<html><head><title>Reporte "+titulo+" </title>"+
        """<style>
        body{
        background: orange;  
        background: -webkit-linear-gradient(to top, red, #FF5733);  
        background: linear-gradient(to top, red, #FF5733); 
        }
        .letra{
            color: White;
        }
        h1, h2{
            color: White;
        }
        </style>
        <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3\" crossorigin=\"anonymous\"><link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css\"></link></head>""")
        report.write("<body><center><h1>Reporte de "+titulo+" </h1><br>")
        report.write("<br>")
        self.printTableToken(report,tokens)
        if titulo =="Errores":
            report.write("<h2>Reporte de "+titulo+" Sintácticos</h2><br>")
            self.printTableError(report,sintactico)
        report.write("</body></html>")
        report.close()
        webbrowser.open("Reporte"+titulo+".html")
    def reporteHTML(self,titulo,registros):
        report = open(titulo+".html","w")
        report.write("<html><head><title>Reporte "+titulo+" </title>"+
        """<style>
        body{
        background: #8e9eab;  
        background: -webkit-linear-gradient(to top, red, #FF5733);  
        background: linear-gradient(to top, red, #FF5733); 
        }
        .letra{
            color: black;
        }
        h1{
            color: White;
        }
        </style>
        <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3\" crossorigin=\"anonymous\"><link rel=\"stylesheet\" href=\"style.css\"></link></head>""")
        report.write("<body><center><h1>"+titulo+" </h1><br>")
        report.write("<br>")
        self.printTable(titulo,report,registros)
        report.write("</body></html>")
        report.close()
        webbrowser.open(titulo+".html")
    def printTable(self,titulo,report,lis):
        report.write("""<div class="container"><table class="table table-light table-striped table-hover">
                                <thead class="letra">""")
        report.write("<tr class=\"table-light\"><th colspan=\""+str(len(lis[0]))+"\">"+titulo+"</th></tr><tr>")
        for campo in lis[0]:
            report.write("<th scope=\"col\">"+campo+"</th>")
        report.write("""                            </tr>
                                </thead>
                                <tbody class="letra">
                                """)
        for i in range(1,len(lis)):
            report.write("<tr>")
            for j in range(len(lis[i])):  
                report.write("<td>"+lis[i][j]+"</td>")
            report.write("</tr>")
        report.write(""" </center></tbody>
                                </table></div>""")