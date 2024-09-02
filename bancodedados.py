import psycopg2


# Conexão com o banco de dados
def conectar():
    try:
        conn = psycopg2.connect(
            dbname="gerenciadoralimentos",
            user="postgres",
            password="33204448",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")


# Criar tabela de alimentos
def criar_tabela():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS alimentos (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        quantidade INTEGER NOT NULL,
        unidade VARCHAR(50) NOT NULL,
        validade DATE NOT NULL
    );
    """)
    conn.commit()
    cur.close()
    conn.close()


# Inserir novo alimento
def inserir_alimento(nome, quantidade, unidade, validade):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO alimentos (nome, quantidade, unidade, validade)
    VALUES (%s, %s, %s, %s);
    """, (nome, quantidade, unidade, validade))
    conn.commit()
    cur.close()
    conn.close()


# Atualizar um alimento existente
def atualizar_alimento(id, nome, quantidade, unidade, validade):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
    UPDATE alimentos 
    SET nome = %s, quantidade = %s, unidade = %s, validade = %s
    WHERE id = %s;
    """, (nome, quantidade, unidade, validade, id))
    conn.commit()
    cur.close()
    conn.close()


# Deletar um alimento
def deletar_alimento(id):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM alimentos WHERE id = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()


# Consultar todos os alimentos
def consultar_alimentos():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM alimentos;")
    alimentos = cur.fetchall()
    cur.close()
    conn.close()
    return alimentos


# Exemplo de uso
if __name__ == "__main__":
    criar_tabela()

    # Inserir alimentos
    inserir_alimento("Maçã", 15, "unidade", "2024-09-30")
    inserir_alimento("Leite", 2, "litro", "2024-09-15")

    # Atualizar alimento
    atualizar_alimento(1, "Maçã Verde", 15, "unidade", "2024-10-01")

    # Consultar alimentos
    alimentos = consultar_alimentos()
    for alimento in alimentos:
        print(alimento)

    # Deletar um alimento
    deletar_alimento(2)

    # Consultar alimentos após deleção
    alimentos = consultar_alimentos()
    for alimento in alimentos:
        print(alimento)
