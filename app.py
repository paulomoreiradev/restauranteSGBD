from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        dbname="RestauranteDB",
        user="postgres",
        password="30201715",
        host="localhost",
        port="5432"
    )
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT mesa.num_mesa, mesa.capacidade, mesa.status, funcionario.nome
        FROM mesa
        JOIN funcionario ON mesa.cod_func = funcionario.cod_func
        ORDER BY mesa.status
    """)

    mesas = cursor.fetchall()
    print(mesas)
    conn.close()
    return render_template("index.html", mesas=mesas)


@app.route("/faturamento")
def faturamento():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM relatorio_faturamento_diario
        WHERE faturamento_total > (SELECT AVG(faturamento_total) FROM relatorio_faturamento_diario);
    """)
    faturamento_diario = cursor.fetchall()
    conn.close()
    return render_template("faturamento_diario.html", faturamento_diario=faturamento_diario)


@app.route("/funcionarios")
def funcionarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT cod_func, nome, email, telefone, cargo FROM funcionario
    """)
    funcionarios = cursor.fetchall()
    conn.close()
    return render_template("funcionarios.html", funcionarios=funcionarios)


@app.route("/funcionarios/criar", methods=["GET"])
def exibir_formulario():
    return render_template("criar_funcionario.html")


@app.route("/funcionarios/criar", methods=["POST"])
def criar_funcionario():
    # Obter os dados do formulário
    cargo = request.form["cargo"]
    nome = request.form["nome"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    rua = request.form["rua"]
    num_end = request.form["num_end"]
    bairro = request.form["bairro"]
    cidade = request.form["cidade"]
    tipo = request.form["tipo"]

    # Conectar ao banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Inserir o novo funcionário
        cursor.execute("""
            INSERT INTO FUNCIONARIO (cargo, nome, email, telefone, rua, num_end, bairro, cidade, tipo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (cargo, nome, email, telefone, rua, num_end, bairro, cidade, tipo))

        # Confirmar a transação
        conn.commit()
    except Exception as e:
        print(f"Erro ao inserir funcionário: {e}")
        conn.rollback()  # Desfazer a transação em caso de erro
    finally:
        conn.close()

    # Redirecionar para a lista de funcionários
    return redirect(url_for("funcionarios"))


@app.route("/funcionarios/excluir/<int:cod_func>", methods=["POST"])
def excluir_funcionario(cod_func):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Excluir o funcionário com o código fornecido
        cursor.execute("DELETE FROM FUNCIONARIO WHERE cod_func = %s", (cod_func,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao excluir funcionário: {e}")
        conn.rollback()  # Desfazer a transação em caso de erro
    finally:
        conn.close()

    # Redirecionar para a lista de funcionários
    return redirect(url_for("funcionarios"))


if __name__ == "__main__":
    app.run(debug=True)