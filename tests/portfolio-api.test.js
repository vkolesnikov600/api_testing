const assert = require('node:assert/strict');
const test = require('node:test');

const BASE_URL = process.env.BASE_URL || 'http://localhost:3000';

async function get(path) {
  return fetch(new URL(path, BASE_URL));
}

test('GET /health returns service status', async () => {
  const response = await get('/health');
  const body = await response.json();

  assert.equal(response.status, 200);
  assert.match(response.headers.get('content-type'), /application\/json/);
  assert.deepEqual(body, { status: 'OK' });
});

test('GET /about returns short profile text', async () => {
  const response = await get('/about');
  const body = await response.text();

  assert.equal(response.status, 200);
  assert.match(response.headers.get('content-type'), /text\/html|text\/plain/);
  assert.equal(body, 'I am QA Engineer');
});

test('GET / returns portfolio HTML page', async () => {
  const response = await get('/');
  const body = await response.text();

  assert.equal(response.status, 200);
  assert.match(response.headers.get('content-type'), /text\/html/);
  assert.match(body, /<title>QA Portfolio<\/title>/);
  assert.match(body, /QA ENGINEER/);
});

test('GET /css/style.css returns stylesheet', async () => {
  const response = await get('/css/style.css');
  const body = await response.text();

  assert.equal(response.status, 200);
  assert.match(response.headers.get('content-type'), /text\/css/);
  assert.match(body, /\.site-header/);
});

test('GET /unknown-route returns 404', async () => {
  const response = await get('/unknown-route');

  assert.equal(response.status, 404);
});
