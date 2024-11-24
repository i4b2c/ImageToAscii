# ImageToAscii

**ImageToAscii** é um script Python que converte qualquer imagem em arte ASCII. Ele utiliza a biblioteca `Pillow` para processar imagens e mapeá-las para um conjunto de caracteres ASCII com base na intensidade de tons de cinza.

## Como Funciona

1. **Redimensionamento da Imagem**: A imagem é redimensionada proporcionalmente para se adequar à largura desejada.
2. **Conversão para Tons de Cinza**: Cada pixel é convertido para um valor de intensidade em escala de cinza.
3. **Mapeamento para ASCII**: Os valores de intensidade são mapeados para um conjunto de caracteres ASCII (do mais escuro para o mais claro).
4. **Saída**: O resultado é salvo em um arquivo `.txt` e pode ser exibido no console.
