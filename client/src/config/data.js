const data = {
  'data': [
    {
      id_topic: '1',
      name: 'Factores Bibliográficos',
      questions: [
        {
          id_question: '1',
          text: 'Nivel educacional',
          inputs: [
            {
              value: '0',
              text: 'Universitaria completa'
            },
            {
              value: '0.25',
              text: 'Universitaria en curso'
            },
            {
              value: '0.5',
              text: 'Técnica completa'
            },
            {
              value: '1',
              text: 'Técnica en curso'
            },
            {
              value: '3',
              text: 'Educación media completa'
            },
            {
              value: '6',
              text: 'Educación básica completa'
            },
            {
              value: '7',
              text: 'N/A'
            }
          ]
        },
        {
          id_question: '2',
          text: 'Experiencia Laboral',
          inputs: [
            {
              value: '0',
              text: 'Ninguna'
            },
            {
              value: '0.25',
              text: 'Más de 1 año'
            },
            {
              value: '0.5',
              text: 'Más de 2 años'
            },
            {
              value: '1',
              text: 'Más de 5 años'
            },
          ]
        }
      ]
    },
    {
      id_topic: '2',
      name: 'Factores Ambientales',
      questions: [
        {
          id_question: '3',
          text: 'Antecedentes penales',
          inputs: [
            {
              value: '0',
              text: 'No'
            },
            {
              value: '0.25',
              text: 'Leve'
            },
            {
              value: '0.5',
              text: 'Grave'
            },
          ]
        },
        {
          id_question: '4',
          text: '¿Cuánto tiempo ha durado en los trabajos?',
          inputs: [
            {
              value: '0',
              text: 'Más de 2 años'
            },
            {
              value: '0.25',
              text: 'Más de 1 año'
            },
            {
              value: '0.5',
              text: 'Más de 6 meses'
            },
            {
              value: '1',
              text: 'N/A'
            },
          ]
        }
      ]
    },
    {
      id_topic: '3',
      name: 'Habilidades, Competencias y Necesidades',
      questions: [
        {
          id_question: '5',
          text: 'tiene la facilidad de relacionarse con otras personas, conocidas o desconocidas',
          inputs: [
            {
              value: '0',
              text: 'Nunca'
            },
            {
              value: '0.25',
              text: 'Poco'
            },
            {
              value: '0.5',
              text: 'Bastante'
            },
            {
              value: '1',
              text: 'Siempre'
            },
          ]
        }
      ],
    }
  ]
}

export default data
