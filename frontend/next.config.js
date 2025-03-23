// next.config.js
module.exports = {
  async redirects() {
    return [
      {
        source: '/',
        destination: '/components/chatbot',
        permanent: true,
      },
    ];
  },
};