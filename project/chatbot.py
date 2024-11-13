from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_response(prompt, model, tokenizer, max_length=100):
    # Encode prompt (input teks) ke dalam bentuk token
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generate teks menggunakan model GPT-2
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id
    )
    
    # Decode output menjadi teks
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    # Load model GPT-2 dan tokenizer
    print("Sedang memuat model GPT-2, mohon tunggu...")
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    print("Model siap! Mulai percakapan dengan chatbot. Ketik 'exit' untuk keluar.")
    while True:
        # Ambil input pengguna
        user_input = input("Anda: ")
        
        # Keluar jika pengguna mengetik 'exit'
        if user_input.lower() == 'exit':
            print("Chatbot: Terima kasih telah menggunakan chatbot ini. Sampai jumpa!")
            break

        # Generate respons dari chatbot
        response = generate_response(user_input, model, tokenizer)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
