def main():
    return """
       <html>
         <body>
           <form action="/eval" method="GET">
             Number 1 : <input name="num_1"/>
             <br>
             Number 2: <input name="num_2"/>
             <br>
             Operator: <input name="operator"/>
             <input type="submit" value="submit">
           </form>
         </body>
       </html>
    """