// crie uma validação de email com regex

export const email = (value: string): boolean => {
    const regex = /\S+@\S+\.\S+/;
    return regex.test(value);
    }

    